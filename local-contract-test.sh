#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_URL="${GPTPROTO_SDK_TEST_BASE_URL:-http://127.0.0.1:8099}"

case "$BASE_URL" in
  http://127.0.0.1:*|http://localhost:*) ;;
  *)
    echo "Refusing non-loopback SDK test base URL: $BASE_URL" >&2
    exit 2
    ;;
esac

: "${GPTPROTO_API_KEY:?Set a test-only GPTPROTO_API_KEY before running this script}"
export GPTPROTO_SDK_TEST_BASE_URL="$BASE_URL"

echo "Running SDK contract checks against $BASE_URL"

(
  cd "$REPO_DIR/gptproto-ts-sdk"
  ./node_modules/.bin/tsx scripts/local_gateway_contract.ts
)
(
  cd "$REPO_DIR/gptproto-python-sdk"
  PYTHONPATH=. "${PYTHON_BIN:-python3}" scripts/local_gateway_contract.py
)
(
  cd "$REPO_DIR/gptproto-go-sdk"
  go test ./gptproto -run TestGatewayErrorContract -count=1
)

echo "All SDKs match the local gateway error contract. No channel task was submitted."
