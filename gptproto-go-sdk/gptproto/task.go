package gptproto

// TaskKind selects one of the stable unified create endpoints.
type TaskKind string

const (
	TaskKindVideo      TaskKind = "video"
	TaskKindImage      TaskKind = "image"
	TaskKindSpeech     TaskKind = "speech"
	TaskKindVoiceClone TaskKind = "voice-clone"
	TaskKindLipSync    TaskKind = "lip-sync"
	TaskKind3D         TaskKind = "3d"
	TaskKindImageTool  TaskKind = "image-tool"
)

func isSuccessStatus(status string) bool {
	return status == "completed"
}

func isFailureStatus(status string) bool {
	switch status {
	case "failed", "cancelled", "expired":
		return true
	default:
		return false
	}
}
