import numpy as np

class GestureController:

    def __init__(self, screen_width, screen_height):
        self.screen_w = screen_width
        self.screen_h = screen_height
        self.prev_pinch_left = False
        self.prev_pinch_right = False
        self.prev_scroll_y = None
        self.smooth_factor = 0.5
        self.prev_cursor_x = 0
        self.prev_cursor_y = 0

    def _fingers_up(self, hand_landmarks):
        
        fingers = []
       
        if hand_landmarks[4][1] > hand_landmarks[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        
        tips_ids = [8, 12, 16, 20]
        pip_ids  = [6, 10, 14, 18]
        for tip, pip in zip(tips_ids, pip_ids):
            if hand_landmarks[tip][2] < hand_landmarks[pip][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def process(self, hand_landmarks, frame_shape):
       
        if not hand_landmarks:
            return "NO_ACTION", {}

        h, w, _ = frame_shape
        fingers = self._fingers_up(hand_landmarks)

        index_tip = hand_landmarks[8]   
        thumb_tip = hand_landmarks[4]
        middle_tip = hand_landmarks[12]

        # ---- 1. SCROLL (index + middle up) ----
        if fingers == [0, 1, 1, 0, 0]:
            curr_y = index_tip[2]   # pixel y
            if self.prev_scroll_y is not None:
                dy = curr_y - self.prev_scroll_y
                if abs(dy) > 15:
                    self.prev_scroll_y = curr_y
                    return "SCROLL", {"delta": -dy // 4} 
            else:
                self.prev_scroll_y = curr_y
            return "NO_ACTION", {}

        
        self.prev_scroll_y = None

       
        if fingers == [0, 1, 0, 0, 0]:
            
            x = np.interp(index_tip[1], (0, w), (0, self.screen_w))
            y = np.interp(index_tip[2], (0, h), (0, self.screen_h))

            
            self.prev_cursor_x = self.prev_cursor_x + self.smooth_factor * (x - self.prev_cursor_x)
            self.prev_cursor_y = self.prev_cursor_y + self.smooth_factor * (y - self.prev_cursor_y)

            return "MOVE", {"x": int(self.prev_cursor_x), "y": int(self.prev_cursor_y)}

        
        if fingers[0] == 1 and fingers[1] == 1:
            # Euclidean distance in pixel space
            dist = np.linalg.norm(np.array(thumb_tip[1:]) - np.array(index_tip[1:]))
            if dist < 30:
                if not self.prev_pinch_left:
                    self.prev_pinch_left = True
                    return "LEFT_CLICK", {}
            else:
                self.prev_pinch_left = False
            return "NO_ACTION", {}

        
        if fingers[0] == 1 and fingers[2] == 1:
            dist = np.linalg.norm(np.array(thumb_tip[1:]) - np.array(middle_tip[1:]))
            if dist < 30:
                if not self.prev_pinch_right:
                    self.prev_pinch_right = True
                    return "RIGHT_CLICK", {}
            else:
                self.prev_pinch_right = False
            return "NO_ACTION", {}

        return "NO_ACTION", {}