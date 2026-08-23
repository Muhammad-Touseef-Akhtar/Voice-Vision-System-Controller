import mediapipe as mp


# ----------------------------------------------------------------------------------------------------------

class Hand_Detection():

    def __init__(self, mode=False, maxHands=2, detection_con=0.7, track_con=0.7):
        self.mode = mode
        self.maxHands = maxHands
        self.detection_con = detection_con
        self.track_con = track_con
    

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detection_con,
                                        min_tracking_confidence=self.track_con)
        self.mpDraw = mp.solutions.drawing_utils
        

    def Find_Hands(self, img, results, draw=True):

        if results.multi_hand_landmarks:
            for hand_lm in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, hand_lm, self.mpHands.HAND_CONNECTIONS)

        return img

    def Find_Hand_Coordinates(self, results,  draw=True):

        land_marks_list = []

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]

            for land_mark in myHand.landmark:
                land_marks_list.append((land_mark.x, land_mark.y))

        return land_marks_list 