package gptproto

import (
	"context"
	"net/url"
	"os"
	"strings"
	"testing"
)

// TestGatewayErrorContract is opt-in: local-contract-test.sh provides both
// environment variables. It only submits an unknown model, so it cannot invoke
// a provider channel.
func TestGatewayErrorContract(t *testing.T) {
	baseURL := os.Getenv("GPTPROTO_SDK_TEST_BASE_URL")
	apiKey := os.Getenv("GPTPROTO_API_KEY")
	if baseURL == "" || apiKey == "" {
		t.Skip("set GPTPROTO_SDK_TEST_BASE_URL and GPTPROTO_API_KEY to run gateway contract test")
	}

	parsed, err := url.Parse(baseURL)
	if err != nil || parsed.Scheme != "http" || (parsed.Hostname() != "127.0.0.1" && parsed.Hostname() != "localhost") {
		t.Fatalf("gateway contract test requires a loopback http URL, got %q", baseURL)
	}

	client := NewClient(apiKey).WithBaseURL(baseURL)
	_, err = client.Create(context.Background(), TaskKindVideo, map[string]any{
		"model":  "sdk-test/not-a-real-model",
		"prompt": "SDK contract probe",
	})
	if err == nil || !strings.Contains(err.Error(), "code=400") {
		t.Fatalf("expected gateway error code 400, got %v", err)
	}
	if !strings.Contains(err.Error(), "unknown video model") {
		t.Fatalf("unexpected gateway error: %v", err)
	}
	t.Log("Go gateway contract: ok")
}
