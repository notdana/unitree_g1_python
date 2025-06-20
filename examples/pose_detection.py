import cv2
import numpy as np
import pyrealsense2 as rs
from ultralytics import YOLO

# Load YOLOv11 pose model (replace with correct model path if local)
model = YOLO("yolo11n-pose.pt")  # or 'yolov11-pose.pt' when available

# Configure RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

try:
    while True:
        # Get RealSense color frame
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        frame = np.asanyarray(color_frame.get_data())

        # Run YOLOv11 pose detection
        results = model.predict(frame, verbose=False)

        # Visualize pose results
        annotated_frame = results[0].plot()

        # Show the frame
        cv2.imshow("YOLOv Pose on RealSense", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
