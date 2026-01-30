import cv2

class VideoSaver:
    def __init__(self, video_capture, output_path="output.mp4", codec="mp4v"):
        """
        video_capture : cv2.VideoCapture object
        output_path   : output video file path
        codec         : video codec (default mp4v)
        """
        self.cap = video_capture
        self.output_path = output_path

        # Read properties from input video
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 30  # fallback

        fourcc = cv2.VideoWriter_fourcc(*codec)
        self.writer = cv2.VideoWriter(
            self.output_path,
            fourcc,
            fps,
            (width, height)
        )

    def write(self, frame):
        """Write a single frame to output video"""
        self.writer.write(frame)

    def release(self):
        """Release the video writer"""
        self.writer.release()
