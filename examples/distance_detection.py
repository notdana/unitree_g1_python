import pyrealsense2 as rs
import numpy as np
import cv2

# Configure the pipeline
pipeline = rs.pipeline()
config = rs.config()

# Enable depth and color streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Find the closest point (excluding 0, which means invalid)
        non_zero_depths = depth_image[depth_image > 0]
        if non_zero_depths.size > 0:
            min_distance = np.min(non_zero_depths)  # in millimeters
        else:
            min_distance = -1  # No valid depth

        # Convert depth image to color for visualization
        depth_colormap = cv2.applyColorMap(
            cv2.convertScaleAbs(depth_image, alpha=0.03),
            cv2.COLORMAP_JET
        )

        # Overlay distance info on the color image
        if min_distance > 0:
            text = f"Closest object: {min_distance} mm"
        else:
            text = "No valid depth data"

        cv2.putText(color_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2)

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))

        # Show the images
        cv2.imshow('RealSense RGB and Depth', images)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop streaming
    pipeline.stop()
    cv2.destroyAllWindows()
