package main

import (
	"encoding/json"
	"fmt"

	"github.com/gptproto-ai/gptproto-sdk/gptproto-go-sdk/gptproto"
)

func main() {
	request := gptproto.NewUnifiedVideoRequest(
		"kling/kling-v3.0-pro",
		"a cat dancing",
	)
	request.SetDuration(5)
	payload, err := json.MarshalIndent(request, "", "  ")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(payload))
}
