#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
TEST_DIR="$(mktemp -d /tmp/gptproto-sdk-verify.XXXXXX)"

cleanup() {
  rm -rf "$TEST_DIR"
}
trap cleanup EXIT

cd "$REPO_DIR"

echo "Linting the public OpenAPI document..."
npx --yes @redocly/cli@1.34.5 lint openapi/openapi.yaml --extends=minimal

echo "Checking public branding..."
INTERNAL_BRAND_PREFIX='blue'
INTERNAL_BRAND_SUFFIX='cat'
INTERNAL_BRAND_PATTERN="${INTERNAL_BRAND_PREFIX}[-_ ]?${INTERNAL_BRAND_SUFFIX}|${INTERNAL_BRAND_PREFIX}${INTERNAL_BRAND_SUFFIX}"
if rg -n -i "$INTERNAL_BRAND_PATTERN" README.md openapi gptproto-ts-sdk gptproto-python-sdk gptproto-go-sdk \
  --glob '!node_modules/**' --glob '!dist/**' --glob '!.venv/**' --glob '!*.egg-info/**'; then
  echo "Internal project branding found in public SDK artifacts." >&2
  exit 1
fi

echo "Building TypeScript SDK..."
(
  cd gptproto-ts-sdk
  npm ci --ignore-scripts
  npm run typecheck
  npm run build
  npm run dev
)

if rg -n '^export type Unified.* = Record<string, any>;' gptproto-ts-sdk/src/generated/models; then
  echo "A public TypeScript request model lost its typed fields." >&2
  exit 1
fi

if [[ -n "${PYTHON_BIN:-}" ]]; then
  PYTHON_CMD="$PYTHON_BIN"
elif command -v python3.11 >/dev/null; then
  PYTHON_CMD="python3.11"
else
  PYTHON_CMD="python3"
fi

echo "Installing and importing Python SDK with $PYTHON_CMD..."
"$PYTHON_CMD" -m venv "$TEST_DIR/venv"
"$TEST_DIR/venv/bin/pip" install --quiet "$REPO_DIR/gptproto-python-sdk"
"$TEST_DIR/venv/bin/python" - <<'PY'
from gptproto import GptprotoClient, TaskKind, UnifiedCreateRequest
from gptproto.models import UnifiedTaskResult, UnifiedVideoRequest, VideoResolution

assert GptprotoClient and TaskKind and UnifiedCreateRequest
assert UnifiedTaskResult and UnifiedVideoRequest and VideoResolution
print("Python SDK import: ok")
PY
"$TEST_DIR/venv/bin/python" "$REPO_DIR/gptproto-python-sdk/examples/demo.py"

echo "Testing Go SDK..."
(
  cd gptproto-go-sdk
  go test ./...
)

echo "All SDK checks passed."
