import cv2
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        # Initialize poseDetector class with optional parameters for customization
        self.mode = mode  # Whether to treat images as static (for one-time detection)
        self.upBody = upBody  # Whether to use a simplified model for upper body
        self.smooth = smooth  # Whether to smooth landmark positions across frames
        self.detectionCon = detectionCon  # Minimum confidence for pose detection
        self.trackCon = trackCon  # Minimum confidence for pose tracking

        # MediaPipe components for pose detection
        self.mpDraw = mp.solutions.drawing_utils  # Utilities for drawing landmarks
        self.mpPose = mp.solutions.pose  # Pose detection module from MediaPipe

         # Initialize the Pose object with the given parameters
        self.pose = self.mpPose.Pose(
            static_image_mode=self.mode, 
            model_complexity=1,  # or 0 depending on your preference
            smooth_landmarks=self.smooth, 
            enable_segmentation=False,  # Whether to enable segmentation 
            smooth_segmentation=False,  # Whether to enable segmentation 
            min_detection_confidence=self.detectionCon, 
            min_tracking_confidence=self.trackCon
        )

    def findPose(self, img, draw=True):
        # Convert the image to RGB for MediaPipe processing
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image and get pose landmarks
        self.results = self.pose.process(imgRGB)

        # Draw landmarks on the image if they are detected
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        # Extract the positions of detected landmarks
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # Convert normalized coordinates to pixel coordinates
                lmList.append([id, cx, cy])  # Add landmark ID and coordinates to list
                
                # Draw circles on landmarks if specified
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)            
        return lmList


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0  
    detector = poseDetector()  # Create an instance of the poseDetector class
    while True:
        # Capture frame-by-frame
        success, img = cap.read()
        if not success:
            break

        # Detect pose and get the landmarks
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # Print and draw specific landmark (e.g., landmark ID 14)
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        # Calculate FPS (frames per second)
        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
        pTime = cTime

        # Display FPS on the image
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
