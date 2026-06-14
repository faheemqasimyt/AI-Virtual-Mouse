import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandDetector:
   
    def __init__(self, model_path='hand_landmarker.task', num_hands=1,
                 min_confidence=0.5):
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=num_hands,
            min_hand_detection_confidence=min_confidence,
            min_tracking_confidence=min_confidence
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.results = None

    def find_hands(self, img, draw=True):
     
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        self.results = self.detector.detect(mp_image)

        if draw and self.results.hand_landmarks:
            h, w, _ = img.shape
            for hand_landmarks in self.results.hand_landmarks:
                # Draw all landmarks as green dots
                for lm in hand_landmarks:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

                # Optionally draw connections (simplified)
                connections = [
                    (0,1), (1,2), (2,3), (3,4),       # thumb
                    (0,5), (5,6), (6,7), (7,8),       # index
                    (0,9), (9,10), (10,11), (11,12),  # middle
                    (0,13), (13,14), (14,15), (15,16),# ring
                    (0,17), (17,18), (18,19), (19,20) # pinky
                ]
                for start, end in connections:
                    x1, y1 = int(hand_landmarks[start].x * w), int(hand_landmarks[start].y * h)
                    x2, y2 = int(hand_landmarks[end].x * w), int(hand_landmarks[end].y * h)
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        return img

    def get_landmark_positions(self, img):
    
        landmark_list = []
        if self.results.hand_landmarks:
            hand = self.results.hand_landmarks[0] #first index hand
            h, w, _ = img.shape
            for idx, lm in enumerate(hand):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append((idx, cx, cy))
        return landmark_list