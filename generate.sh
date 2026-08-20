#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SPEC="$REPO_DIR/openapi/openapi.yaml"
WORK_DIR="$(mktemp -d /tmp/gptproto-sdk-generate.XXXXXX)"
GENERATOR_VERSION="6.6.0"
PYTHON_CLIENT_VERSION="0.29.0"
JAVA_BIN="${JAVA_BIN:-java}"

cleanup() {
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT

command -v npm >/dev/null
command -v uvx >/dev/null
command -v curl >/dev/null
command -v "$JAVA_BIN" >/dev/null

echo "Generating TypeScript models and services..."
(
  cd "$REPO_DIR/gptproto-ts-sdk"
  npm ci --ignore-scripts
  find src/generated -mindepth 1 -delete
  npm run generate
)

echo "Generating Python models, services, and transport..."
uvx --from "openapi-python-client==$PYTHON_CLIENT_VERSION" openapi-python-client generate \
  --path "$SPEC" \
  --config "$REPO_DIR/openapi/python-codegen.yaml" \
  --output-path "$WORK_DIR/python" \
  --meta none \
  --overwrite
rsync -a --delete "$WORK_DIR/python/api/" "$REPO_DIR/gptproto-python-sdk/gptproto/api/"
rsync -a --delete "$WORK_DIR/python/models/" "$REPO_DIR/gptproto-python-sdk/gptproto/models/"
cp "$WORK_DIR/python/client.py" "$REPO_DIR/gptproto-python-sdk/gptproto/client.py"
cp "$WORK_DIR/python/errors.py" "$REPO_DIR/gptproto-python-sdk/gptproto/errors.py"
cp "$WORK_DIR/python/types.py" "$REPO_DIR/gptproto-python-sdk/gptproto/types.py"

echo "Generating Go models..."
GENERATOR_JAR="$WORK_DIR/openapi-generator-cli.jar"
curl --fail --location --silent --show-error \
  --output "$GENERATOR_JAR" \
  "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$GENERATOR_VERSION/openapi-generator-cli-$GENERATOR_VERSION.jar"
generate_go() {
  "$JAVA_BIN" "$@" -jar "$GENERATOR_JAR" generate \
    -i "$SPEC" \
    -g go \
    -o "$WORK_DIR/go" \
    --git-user-id gptproto \
    --git-repo-id gptproto-go-sdk \
    --additional-properties='packageName=gptproto,packageVersion=0.1.0,enumClassPrefix=true' \
    --global-property='models,supportingFiles=utils.go,apiTests=false,modelTests=false,apiDocs=false,modelDocs=false'
}
if "$JAVA_BIN" -version 2>&1 | head -n 1 | grep -q '"1\.8\.'; then
  generate_go
else
  generate_go \
    --add-opens java.base/java.util=ALL-UNNAMED \
    --add-opens java.base/java.lang=ALL-UNNAMED
fi
find "$REPO_DIR/gptproto-go-sdk/gptproto" -maxdepth 1 -type f -name 'model_*.go' -delete
cp "$WORK_DIR/go"/model_*.go "$REPO_DIR/gptproto-go-sdk/gptproto/"
cp "$WORK_DIR/go/utils.go" "$REPO_DIR/gptproto-go-sdk/gptproto/utils.go"
gofmt -w "$REPO_DIR/gptproto-go-sdk/gptproto"

echo "Generation complete. Hand-written create/poll layers were preserved."
