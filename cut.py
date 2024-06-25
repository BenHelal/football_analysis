import cv2
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector

def detect_scenes(video_path, threshold=30.0):
    # Create a video manager object
    video_manager = VideoManager([video_path])
    # Create a scene manager object
    scene_manager = SceneManager()
    # Add ContentDetector algorithm (detects fast cuts)
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    
    # Start video manager and perform scene detection
    video_manager.set_downscale_factor()
    video_manager.start()
    
    scene_manager.detect_scenes(frame_source=video_manager)
    
    # List of scenes found
    scene_list = scene_manager.get_scene_list()
    
    video_manager.release()
    
    return scene_list

def cut_video(video_path, scene_list, output_folder):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    for i, (start_time, end_time) in enumerate(scene_list):
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_time.get_frames())
        
        out = cv2.VideoWriter(f'{output_folder}/scene_{i+1}.avi', fourcc, frame_rate, (frame_width, frame_height))
        
        for j in range(start_time.get_frames(), end_time.get_frames()):
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
        
        out.release()
    
    cap.release()

def main():
    video_path = 'input_videos/Türkiye vs Portugal Full Highlights  EURO2024.mp4'
    output_folder = 'output_videos'
    
    print("Detecting scenes...")
    scene_list = detect_scenes(video_path)
    print(f"Found {len(scene_list)} scenes.")
    
    print("Cutting video...")
    cut_video(video_path, scene_list, output_folder)
    print("Done.")

if __name__ == '__main__':
    main()
