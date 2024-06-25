# Football Analysis Project

## Introduction
The goal of this project is to detect and track players, referees, and footballs in a video using YOLO, one of the best AI object detection models available. We will also train the model to improve its performance. Additionally, we will assign players to teams based on the colors of their t-shirts using Kmeans for pixel segmentation and clustering. With this information, we can measure a team's ball acquisition percentage in a match.

We will also use optical flow to measure camera movement between frames, enabling us to accurately measure a player's movement. Furthermore, we will implement perspective transformation to represent the scene's depth and perspective, allowing us to measure a player's movement in meters rather than pixels. Finally, we will calculate a player's speed and the distance covered.

This project covers various concepts and addresses real-world problems, making it suitable for both beginners and experienced machine learning engineers.

## Screenshot
![screenshot](https://github.com/BenHelal/football_analysis/assets/114242095/4c30de94-39bd-41c9-997f-279fb8c992a3)


## Modules Used
The following modules are used in this project:
- **YOLO**: AI object detection model
- **Kmeans**: Pixel segmentation and clustering to detect t-shirt color
- **Optical Flow**: Measure camera movement
- **Perspective Transformation**: Represent scene depth and perspective
- **Speed and Distance Calculation per Player**

## Trained Models
- Trained YOLO v5

## Sample Video
- [Sample Input Video](path_to_sample_video)

## Requirements
To run this project, you need to have the following requirements installed:
- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/football-analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd football-analysis
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the main script to start the analysis:
    ```bash
    python main.py
    ```

2. To use your own video, replace the sample video path with your video path in the script:
    ```python
    video_path = "path_to_your_video"
    ```

## Contributing
Feel free to fork the repository and submit pull requests. Any contributions are highly appreciated!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or suggestions, please feel free to contact me at [your_email@example.com](mailto:your_email@example.com).
