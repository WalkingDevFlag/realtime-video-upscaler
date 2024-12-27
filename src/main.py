import os
import cv2
from video import convert_video_fps

def main():
    # Define the input and output video paths
    input_video_path = r"E:/GitHub/realtime-video-upscaler/input/input.mp4"  
    output_video_path = r"E:/GitHub/realtime-video-upscaler/output/output.mp4"  
    
    if not os.path.exists(input_video_path):
        print(f"Error: The file {input_video_path} does not exist.")
        return
    
    convert_video_fps(input_video_path, output_video_path)

    '''
    # Check total Frames
    cap = cv2.VideoCapture(output_video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)
    '''
    
if __name__ == "__main__":
    main()
