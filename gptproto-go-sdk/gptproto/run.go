package gptproto

import (
	"context"
	"fmt"
	"time"
)

// TaskFailedError is returned when a task reaches a failed terminal state.
type TaskFailedError struct {
	TaskID string
	Status string
	Err    string
}

func (e *TaskFailedError) Error() string {
	return fmt.Sprintf("task %s ended with %s: %s", e.TaskID, e.Status, e.Err)
}

// TaskTimeoutError is returned when polling times out. The task remains queryable with Get.
type TaskTimeoutError struct {
	TaskID string
}

func (e *TaskTimeoutError) Error() string {
	return fmt.Sprintf("task %s polling timeout", e.TaskID)
}

// RunOptions configures the polling loop.
type RunOptions struct {
	Timeout      time.Duration
	PollInterval time.Duration
	OnStatus     func(taskID, status string)
}

// Run submits and polls a task until it reaches a terminal unified status.
func (c *Client) Run(ctx context.Context, kind TaskKind, body any, opts *RunOptions) (*UnifiedTaskResult, error) {
	if opts == nil {
		opts = &RunOptions{}
	}
	timeout := opts.Timeout
	if timeout == 0 {
		timeout = 10 * time.Minute
	}
	interval := opts.PollInterval
	if interval == 0 {
		interval = 3 * time.Second
	}

	created, err := c.Create(ctx, kind, body)
	if err != nil {
		return nil, err
	}
	deadline := time.Now().Add(timeout)
	for time.Now().Before(deadline) {
		select {
		case <-ctx.Done():
			return nil, ctx.Err()
		case <-time.After(interval):
		}

		result, err := c.Get(ctx, created.Id, kind)
		if err != nil {
			return nil, err
		}
		if opts.OnStatus != nil {
			opts.OnStatus(created.Id, result.Status)
		}
		if isSuccessStatus(result.Status) {
			return result, nil
		}
		if isFailureStatus(result.Status) {
			errMessage := "unknown"
			if result.Error != nil && *result.Error != "" {
				errMessage = *result.Error
			}
			return nil, &TaskFailedError{TaskID: created.Id, Status: result.Status, Err: errMessage}
		}
	}
	return nil, &TaskTimeoutError{TaskID: created.Id}
}
