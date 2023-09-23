import math
from sndhdr import what
import cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

# Setting up the Pose function.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

# Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils


def detectPose(image, pose, display=True):
    
    # Create a copy of the input image.
    output_image = image.copy()
    
    # Convert the image from BGR into RGB format.
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform the Pose Detection.
    results = pose.process(imageRGB)
    
    # Retrieve the height and width of the input image.
    height, width, _ = image.shape
    
    # Initialize a list to store the detected landmarks.
    landmarks = []
    
    # Check if any landmarks are detected.
    if results.pose_landmarks:
    
        # Draw Pose landmarks on the output image.
        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS)
        
        # Iterate over the detected landmarks.
        for landmark in results.pose_landmarks.landmark:
            
            # Append the landmark into the list.
            landmarks.append((int(landmark.x * width), int(landmark.y * height),
                                  (landmark.z * width)))
    
    # Check if the original input image and the resultant image are specified to be displayed.
    if display:
    
        # Display the original input image and the resultant image.
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        
        # Also Plot the Pose landmarks in 3D.
        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        
    # Otherwise
    else:
        # Return the output image and the found landmarks.
        return output_image, landmarks

def calculateAngle(landmark1, landmark2, landmark3):
    # Get the required landmarks coordinates.
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3

    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    # Check if the angle is less than zero.
    if angle < 0:

        # Add 360 to the found angle.
        angle += 360
    
    # Return the calculated angle.
    return angle


def backwardlungef(whattype,till,camera):
    pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)
    camera_video = cv2.VideoCapture(int(camera))
    camera_video.set(3,1280)
    camera_video.set(4,960)
    cv2.namedWindow('BACKWARD LUNGE', cv2.WINDOW_NORMAL)
    count=0
    up=0
    down=0
    rightnow="down"
    sec=0
    while camera_video.isOpened():
        sec+=1
        ok, frame = camera_video.read()
        
        if not ok:
            continue
        
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ =  frame.shape
        frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
        frame, landmarks = detectPose(frame, pose_video, display=False)
        
        if landmarks:
            angle1 = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
            angle2 = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
            angle3 = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
            angle4 = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
            angle5 = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])
            angle6 = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value], landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])
            angle7 = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value], landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])
            angle8 =calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])
            angle9 = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value], landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
            angle10 = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value], landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

            su=20
            font=2
            color = (250, 0, 83)
        
            cv2.rectangle(frame, (0, 0), (225, 73), (0, 0, 255), -1)
        
            cv2.putText(frame, 'BACKWARD LUNGE', (65,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

            


            if angle9<=100  and angle10<=100   and rightnow=="down":
                up+=1
                rightnow="up"
            if angle9>=170  and angle10<=190 and rightnow=="up":
                rightnow="down"
                down+=1
                count+=1



            


            if whattype=="sets":
                cv2.putText(frame, str(count)+" sets",(10, 60),cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2, cv2.LINE_AA)
            if whattype=="time":
                cv2.putText(frame, str(till-int(sec/10))+" secs",(10, 60),cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('BACKWARD LUNGE', frame)
        
        k = cv2.waitKey(1) & 0xFF
        
        if whattype=="sets" and till==count:
            break
        if whattype=="time" and till==int(sec/10):
            break
        if(k == 27):
            break
        

    camera_video.release()
    cv2.destroyAllWindows()

    return count,int(sec/10)
