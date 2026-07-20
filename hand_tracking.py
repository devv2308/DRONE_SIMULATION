import cv2
import mediapipe as mp

class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.draw = mp.solutions.drawing_utils

    def findHand(self, img):

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        lmList = []

        if result.multi_hand_landmarks:

            for hand in result.multi_hand_landmarks:

                self.draw.draw_landmarks(
                    img,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

                h, w, _ = img.shape

                for id, lm in enumerate(hand.landmark):

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    lmList.append((id, cx, cy))

        return img, lmList