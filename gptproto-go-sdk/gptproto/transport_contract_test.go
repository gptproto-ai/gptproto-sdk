package gptproto

import (
	"context"
	"os"
	"strings"
	"testing"
	"time"
)

// TestLocalTransportContract is enabled only by local-transport-test.sh. Its
// mock is loopback-only and validates every public create route plus both GET routes.
func TestLocalTransportContract(t *testing.T) {
	baseURL := os.Getenv("GPTPROTO_SDK_TEST_BASE_URL")
	if baseURL == "" || os.Getenv("GPTPROTO_SDK_TRANSPORT_TEST") != "1" {
		t.Skip("run via local-transport-test.sh")
	}
	if !strings.HasPrefix(baseURL, "http://127.0.0.1:") && !strings.HasPrefix(baseURL, "http://localhost:") {
		t.Fatalf("requires loopback test URL, got %q", baseURL)
	}
	client := NewClient("").WithBaseURL(baseURL)
	requests := []struct {
		kind TaskKind
		body map[string]any
	}{
		{TaskKindVideo, map[string]any{"model": "test/video", "prompt": "test"}},
		{TaskKindImage, map[string]any{"model": "test/image", "prompt": "test"}},
		{TaskKindSpeech, map[string]any{"model": "test/speech", "input": "test", "voice": "test"}},
		{TaskKindVoiceClone, map[string]any{"model": "test/voice-clone", "audio": "https://example.invalid/audio.mp3"}},
		{TaskKindLipSync, map[string]any{"model": "test/lip-sync", "video": "https://example.invalid/video.mp4", "audio": "https://example.invalid/audio.mp3"}},
		{TaskKind3D, map[string]any{"model": "test/3d", "image": "https://example.invalid/image.png"}},
		{TaskKindImageTool, map[string]any{"model": "test/image-tool", "image": "https://example.invalid/image.png"}},
	}
	for _, request := range requests {
		result, err := client.Create(context.Background(), request.kind, request.body)
		if err != nil || result.Status != "pending" || !strings.HasPrefix(result.Id, "local-") {
			t.Fatalf("create %s: result=%#v err=%v", request.kind, result, err)
		}
	}
	for _, kind := range []TaskKind{TaskKindVideo, TaskKindImage} {
		result, err := client.Get(context.Background(), "local-check", kind)
		if err != nil || result.Status != "completed" {
			t.Fatalf("get %s: result=%#v err=%v", kind, result, err)
		}
	}
	result, err := client.Run(context.Background(), TaskKindVideo, map[string]any{"model": "test/video", "prompt": "test"}, &RunOptions{Timeout: time.Second, PollInterval: time.Millisecond})
	if err != nil || result.Status != "completed" {
		t.Fatalf("run: result=%#v err=%v", result, err)
	}
}
