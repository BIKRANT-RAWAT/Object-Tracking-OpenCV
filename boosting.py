import cv2
from video_writer import VideoSaver

def main():
    # Initialize Boosting Tracker
    tracker = cv2.legacy.TrackerBoosting_create()

    # Open webcam or video file
    video = cv2.VideoCapture("Eagle.mp4")  # Replace 0 with video path for webcam

    # Read the first frame
    ret, frame = video.read()
    if not ret:
        print("Failed to read from video source")
        video.release()
        return

    # Select ROI (object to track)
    bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()

    # Initialize the tracker with the selected ROI
    tracker.init(frame, bbox)

    saver = VideoSaver(video, output_path="tracking_output.mp4")

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Update the tracker
        success, bbox = tracker.update(frame)

        if success:
            # Tracking success: draw bounding box
            x, y, w, h = map(int, bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        
        saver.write(frame) 

        # Display result
        cv2.imshow("Boosting Tracker", frame)

        # Exit on ESC key
        key = cv2.waitKey(30) & 0xFF
        if key == 27:
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()