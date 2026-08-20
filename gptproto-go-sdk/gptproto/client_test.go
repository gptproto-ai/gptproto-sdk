package gptproto

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestCreateRoutesAndPayload(t *testing.T) {
	tests := []struct {
		kind TaskKind
		path string
	}{
		{TaskKindVideo, "/api/v3/videos"},
		{TaskKindImage, "/api/v3/images"},
		{TaskKindSpeech, "/api/v3/audio/speech"},
		{TaskKindVoiceClone, "/api/v3/audio/voice-clone"},
		{TaskKindLipSync, "/api/v3/lip-sync"},
		{TaskKind3D, "/api/v3/3d"},
		{TaskKindImageTool, "/api/v3/images/edit"},
	}

	for _, test := range tests {
		t.Run(string(test.kind), func(t *testing.T) {
			server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				if r.Method != http.MethodPost || r.URL.Path != test.path {
					t.Fatalf("request = %s %s, want POST %s", r.Method, r.URL.Path, test.path)
				}
				if got := r.Header.Get("Authorization"); got != "Bearer test-key" {
					t.Fatalf("Authorization = %q", got)
				}
				var body map[string]any
				if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
					t.Fatal(err)
				}
				if body["model"] != "vendor/model" || body["custom"] != "kept" {
					t.Fatalf("unexpected body: %#v", body)
				}
				w.Header().Set("Content-Type", "application/json")
				w.WriteHeader(http.StatusAccepted)
				_, _ = w.Write([]byte(`{"id":"task-1","status":"pending","polling_url":"/poll/task-1"}`))
			}))
			defer server.Close()

			client := NewClient("test-key").WithBaseURL(server.URL)
			result, err := client.Create(context.Background(), test.kind, map[string]any{
				"model":  "vendor/model",
				"custom": "kept",
			})
			if err != nil {
				t.Fatal(err)
			}
			if result.Id != "task-1" || result.Status != "pending" {
				t.Fatalf("unexpected result: %#v", result)
			}
		})
	}
}

func TestGetUsesCanonicalPaths(t *testing.T) {
	var paths []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		paths = append(paths, r.RequestURI)
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"id":"task/id","status":"completed","polling_url":"/poll"}`))
	}))
	defer server.Close()

	client := NewClient("test-key").WithBaseURL(server.URL)
	if _, err := client.Get(context.Background(), "task/id", TaskKindVideo); err != nil {
		t.Fatal(err)
	}
	if _, err := client.Get(context.Background(), "task/id", TaskKindImage); err != nil {
		t.Fatal(err)
	}

	want := []string{"/api/v3/videos/task%2Fid", "/api/v3/tasks/result/task%2Fid"}
	for i := range want {
		if paths[i] != want[i] {
			t.Fatalf("path[%d] = %q, want %q", i, paths[i], want[i])
		}
	}
}

func TestCreateReturnsStructuredAPIError(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusBadRequest)
		_, _ = w.Write([]byte(`{"error":{"message":"invalid model","code":4001}}`))
	}))
	defer server.Close()

	client := NewClient("test-key").WithBaseURL(server.URL)
	_, err := client.Create(context.Background(), TaskKindVideo, map[string]any{"model": "bad"})
	if err == nil || err.Error() != "request rejected: code=4001 message=invalid model" {
		t.Fatalf("unexpected error: %v", err)
	}
}
