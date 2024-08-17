# Bicep Curl Counter

This project uses OpenCV and Mediapipe library to detect human poses in real-time 
through a webcam feed and count bicep curls. The system tracks the position of key landmarks on the user's arm to calculate the angle between the shoulder, elbow, and wrist. When the angle indicates a full curl (from the arm fully extended to fully bent), the counter increments.

## Pose Landmark Model
The landmark model in MediaPipe Pose predicts the location of 33 pose landmarks (see figure below).
![pose_landmark](https://github.com/user-attachments/assets/c56132a5-f15e-49ac-b842-6b60f4fe191b)

Optionally, MediaPipe Pose can predict a full-body segmentation mask represented as a two-class segmentation (human or background).

## Features
- Real-Time Pose Detection: Uses the Mediapipe library to detect key points on the body.
- Angle Calculation: Calculates the angle between the shoulder, elbow, and wrist to determine the stage of the curl.
- Curl Counter: Automatically counts the number of bicep curls based on the angle.
- Visual Feedback: Displays the current angle and the count of completed curls on the screen.

## Dependencies
- Python 3.x
- OpenCV
- Mediapipe
- Numpy
- math

You can install the required libraries using pip:
```sh
pip install opencv-python mediapipe numpy
```

## How It Works
1. Capture Video: The program captures live video from the default camera.
2. Pose Detection: Mediapipe's Pose module is used to detect the position of the shoulder, elbow, and wrist.
3. Angle Calculation: The angle between these landmarks is calculated.
4. Curl Counting: When the angle changes from a large to a small value (indicating a curl), the counter increments.
5. Visual Display: The angle, stage, and count are displayed on the video feed.

## Usage
1. Clone the repository:
```sh
git clone https://github.com/SachinSingh1402/AI_Pose_Estimation.git
cd bicep-curl-counter
```
2. Run the Python script:
```sh
python Pose_Tutorial.py
```
3.The webcam feed will open, and the program will start detecting and counting curls.
4.Press `q` to quit the program.

## Code Explanation
- `mp_drawing` and `mp_pose`: Initialize Mediapipe's drawing utilities and pose module.
- `cap = cv2.VideoCapture(0)`: Opens the webcam feed.
- Angle Calculation: The angle between shoulder, elbow, and wrist is calculated using the `calculate_angle` function (you'll need to define this function).
- Curl Counter: The code checks if the arm is fully extended or bent and counts a curl when the arm is fully bent after being fully extended.

## Example Output
The following images demonstrate the output of the program:
- Pose Estimation: This image shows the detected pose landmarks.
- Curl Counter: This image shows the real-time count of curls and the stage of the curl (up/down).

https://github.com/user-attachments/assets/e21c6f85-2eb7-470a-bdbc-3f1729b9db19

## License
This project is licensed under the MIT License - see the LICENSE file for details.
