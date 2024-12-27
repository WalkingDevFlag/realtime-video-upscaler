import cv2
import numpy as np

def convert_video_fps(input_video_path, output_video_path, target_fps=15):
    """
    Converts the frame rate of a video to a specified target FPS.

    Parameters:
    - input_video_path (str): Path to the input video file.
    - output_video_path (str): Path where the output video will be saved.
    - target_fps (int): The desired frames per second for the output video. Default is 15 FPS.

    The function opens the input video, retrieves its properties (original FPS, resolution, total frames),
    and writes a new video file at the specified target FPS by skipping frames as necessary.
    """
    
    # Open the input video using OpenCV
    cap = cv2.VideoCapture(input_video_path)
    
    if not cap.isOpened():
        print(f"Error: Couldn't open the video file {input_video_path}")
        return
    
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Original FPS: {original_fps}")
    print(f"Video resolution: {width}x{height}")
    print(f"Total frames: {total_frames}")
    
    # Set up the video writer for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or *'avc1' or *'XVID' or *'h264'
    out = cv2.VideoWriter(output_video_path, fourcc, target_fps, (width, height))
    frame_interval = int(original_fps / target_fps)  # Skip frames to match target FPS
    
    # Start capturing frames
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            out.write(frame)
        
        frame_count += 1

    cap.release()
    out.release()
    print(f"Video conversion complete. Output saved to {output_video_path}")


'''
if __name__ == "__main__":
    input_video_path = 'input_video.mp4'  # Replace with your video file path
    output_video_path = 'output_video_15fps.mp4'  # Desired output video path
    convert_video_fps(input_video_path, output_video_path)
'''
