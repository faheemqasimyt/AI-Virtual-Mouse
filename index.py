import cv2
import pyautogui
from Function.handDetector import HandDetector
from Function.gesture_control import GestureController
from Function.mouse_actions import execute_action

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    detector = HandDetector(model_path='hand_landmarker.task')
    screen_w, screen_h = pyautogui.size()
    controller = GestureController(screen_w, screen_h)

    print("AI Virtual Mouse. Press 'q' to quit.")
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame = detector.find_hands(frame)
        landmarks = detector.get_landmark_positions(frame)

        if landmarks:
            action, params = controller.process(landmarks, frame.shape)
            execute_action(action, params)
            cv2.putText(frame, f"Action: {action}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("AI Virtual Mouse", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()