// Package gptproto provides a client for the GPTProto unified asynchronous
// media API. Request and response models are generated from openapi/openapi.yaml;
// this file is the small hand-written HTTP layer.
package gptproto

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
)

const defaultBaseURL = "https://gptproto.com"

var createPaths = map[TaskKind]string{
	TaskKindVideo:      "/api/v3/videos",
	TaskKindImage:      "/api/v3/images",
	TaskKindSpeech:     "/api/v3/audio/speech",
	TaskKindVoiceClone: "/api/v3/audio/voice-clone",
	TaskKindLipSync:    "/api/v3/lip-sync",
	TaskKind3D:         "/api/v3/3d",
	TaskKindImageTool:  "/api/v3/images/edit",
}

// Client is the GPTProto API client.
type Client struct {
	apiKey     string
	baseURL    string
	httpClient *http.Client
}

// NewClient creates a client. If apiKey is empty, GPTPROTO_API_KEY is used.
func NewClient(apiKey string) *Client {
	if apiKey == "" {
		apiKey = os.Getenv("GPTPROTO_API_KEY")
	}
	return &Client{
		apiKey:     apiKey,
		baseURL:    defaultBaseURL,
		httpClient: &http.Client{Timeout: 30 * time.Second},
	}
}

// WithBaseURL overrides the API origin, primarily for self-hosted deployments and tests.
func (c *Client) WithBaseURL(baseURL string) *Client {
	c.baseURL = strings.TrimRight(baseURL, "/")
	return c
}

// WithHTTPClient overrides the underlying HTTP client.
func (c *Client) WithHTTPClient(httpClient *http.Client) *Client {
	c.httpClient = httpClient
	return c
}

// Create submits a task through the canonical endpoint selected by kind.
func (c *Client) Create(ctx context.Context, kind TaskKind, body any) (*UnifiedTaskResult, error) {
	path, ok := createPaths[kind]
	if !ok {
		return nil, fmt.Errorf("unsupported task kind %q", kind)
	}
	return c.request(ctx, http.MethodPost, path, body, http.StatusAccepted)
}

// Get queries a task once. Video tasks have a canonical video query endpoint;
// all other task kinds use the shared task-result endpoint.
func (c *Client) Get(ctx context.Context, taskID string, kind TaskKind) (*UnifiedTaskResult, error) {
	path := "/api/v3/tasks/result/" + url.PathEscape(taskID)
	if kind == TaskKindVideo {
		path = "/api/v3/videos/" + url.PathEscape(taskID)
	}
	return c.request(ctx, http.MethodGet, path, nil, http.StatusOK)
}

func (c *Client) request(ctx context.Context, method, path string, body any, wantStatus int) (*UnifiedTaskResult, error) {
	if c.apiKey == "" {
		return nil, fmt.Errorf("missing API key: pass it to NewClient or set GPTPROTO_API_KEY")
	}

	var reader io.Reader
	if body != nil {
		payload, err := json.Marshal(body)
		if err != nil {
			return nil, fmt.Errorf("marshal request body: %w", err)
		}
		reader = bytes.NewReader(payload)
	}
	req, err := http.NewRequestWithContext(ctx, method, strings.TrimRight(c.baseURL, "/")+path, reader)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	if body != nil {
		req.Header.Set("Content-Type", "application/json")
	}

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	raw, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("read response: %w", err)
	}
	if resp.StatusCode != wantStatus {
		var apiErr UnifiedErrorResponse
		if json.Unmarshal(raw, &apiErr) == nil && apiErr.Error.Message != "" {
			return nil, fmt.Errorf("request rejected: code=%d message=%s", apiErr.Error.Code, apiErr.Error.Message)
		}
		return nil, fmt.Errorf("request failed: status=%d body=%s", resp.StatusCode, string(raw))
	}

	var result UnifiedTaskResult
	if err := json.Unmarshal(raw, &result); err != nil {
		return nil, fmt.Errorf("decode task response: %w", err)
	}
	if result.Id == "" {
		return nil, fmt.Errorf("task response has empty id")
	}
	return &result, nil
}
