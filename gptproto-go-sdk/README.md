# GPTProto Go SDK

Go client for the GPTProto unified asynchronous media API. OpenAPI-generated
models live beside a small hand-written HTTP and polling layer.

## Use

```bash
go get github.com/gptproto-ai/gptproto-sdk/gptproto-go-sdk
export GPTPROTO_API_KEY=your_key
```

```go
client := gptproto.NewClient("")
request := gptproto.NewUnifiedVideoRequest(
    "kling/kling-v3.0-pro",
    "a cat dancing",
)
request.SetDuration(5)

result, err := client.Run(ctx, gptproto.TaskKindVideo, request, &gptproto.RunOptions{
    OnStatus: func(id, status string) { fmt.Println(id, status) },
})
if err != nil {
    log.Fatal(err)
}
fmt.Println(result.UnsignedUrls)
```

Task kinds are exposed as `TaskKindVideo`, `TaskKindImage`, `TaskKindSpeech`,
`TaskKindVoiceClone`, `TaskKindLipSync`, `TaskKind3D`, and
`TaskKindImageTool`. Use `Create` and `Get` for manual polling.

## Develop

```bash
go test ./...
go run ./examples
```

Use the repository-level `../generate.sh` to refresh generated model files
without overwriting `client.go`, `task.go`, or `run.go`.
