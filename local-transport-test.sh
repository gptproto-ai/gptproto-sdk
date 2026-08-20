#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PORT="${GPTPROTO_SDK_TRANSPORT_PORT:-18082}"
BASE_URL="http://127.0.0.1:${PORT}"
export GPTPROTO_SDK_TEST_BASE_URL="$BASE_URL"
export GPTPROTO_API_KEY="${GPTPROTO_API_KEY:-local-sdk-test-key}"
export GPTPROTO_SDK_TRANSPORT_TEST=1

cleanup() {
  if [[ -n "${SERVER_PID:-}" ]]; then kill "$SERVER_PID" 2>/dev/null || true; fi
}
trap cleanup EXIT

node "$REPO_DIR/scripts/local_sdk_transport_server.mjs" >"${TMPDIR:-/tmp}/gptproto-sdk-transport-${PORT}.log" 2>&1 &
SERVER_PID=$!
for _ in {1..40}; do
  if curl --silent "$BASE_URL/noop" >/dev/null 2>&1; then break; fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then cat "${TMPDIR:-/tmp}/gptproto-sdk-transport-${PORT}.log" >&2; exit 1; fi
  sleep 0.1
done

(
  cd "$REPO_DIR/gptproto-ts-sdk"
  ./node_modules/.bin/tsx scripts/local_transport_contract.ts
)
(
  cd "$REPO_DIR/gptproto-python-sdk"
  PYTHONPATH=. "${PYTHON_BIN:-python3}" scripts/local_transport_contract.py
)
(
  cd "$REPO_DIR/gptproto-go-sdk"
  go test ./gptproto -run TestLocalTransportContract -count=1
)
echo "All SDKs passed the loopback create/get/run transport contract."
