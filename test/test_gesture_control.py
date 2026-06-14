import pytest
from Function.gesture_control import GestureController

SCREEN_W = 1920
SCREEN_H = 1080


@pytest.fixture
def controller():
    return GestureController(SCREEN_W, SCREEN_H)


def make_landmarks(positions):
    landmarks = []
    for idx, (x, y) in enumerate(positions):
        landmarks.append((idx, x, y))
    return landmarks


def test_move_cursor(controller):

    frame_shape = (720, 1280, 3)

    landmarks = [(i, 0, 400) for i in range(21)]  # all fingers down initially

    landmarks[4] = (4, 500, 450)
    landmarks[3] = (3, 400, 450)

    landmarks[4] = (4, 300, 450)
    landmarks[3] = (3, 400, 450)

    landmarks[8] = (8, 640, 200)
    landmarks[6] = (6, 640, 300)

    action, params = controller.process(landmarks, frame_shape)

    expected_x = 640 * SCREEN_W / 1280
    expected_y = 200 * SCREEN_H / 720

    assert action == "MOVE"
    assert "x" in params and "y" in params
    assert 0 <= params["x"] <= SCREEN_W
    assert 0 <= params["y"] <= SCREEN_H


def test_left_click_pinch(controller):

    frame_shape = (720, 1280, 3)
    # Thumb up: tip.x > ip.x
    landmarks = [(i, 0, 400) for i in range(21)]
    landmarks[3] = (3, 200, 500)
    landmarks[4] = (4, 220, 500)
    landmarks[6] = (6, 300, 400)
    landmarks[8] = (8, 300, 200)

    landmarks[4] = (4, 300, 200)
    action, params = controller.process(landmarks, frame_shape)
    assert action == "LEFT_CLICK"


def test_right_click_pinch(controller):

    frame_shape = (720, 1280, 3)
    landmarks = [(i, 0, 400) for i in range(21)]

    landmarks[3] = (3, 200, 500)
    landmarks[4] = (4, 220, 500)

    landmarks[10] = (10, 400, 400)
    landmarks[12] = (12, 400, 200)
    landmarks[4] = (4, 400, 200)
    action, params = controller.process(landmarks, frame_shape)
    assert action == "RIGHT_CLICK"


def test_scroll(controller):

    frame_shape = (720, 1280, 3)
    landmarks = [(i, 0, 400) for i in range(21)]
    landmarks[6] = (6, 500, 300)
    landmarks[10] = (10, 600, 300)
    landmarks[12] = (12, 600, 100)

    action1, _ = controller.process(landmarks, frame_shape)
    assert action1 == "NO_ACTION"

    landmarks[8] = (8, 500, 200)
    action2, params = controller.process(landmarks, frame_shape)

    assert action2 == "SCROLL"

    assert params["delta"] == -25


def test_no_action_when_no_landmarks(controller):
    action, params = controller.process([], (720, 1280, 3))
    assert action == "NO_ACTION"


def test_multiple_calls_smooth_movement(controller):
    frame_shape = (720, 1280, 3)
    landmarks = [(i, 0, 400) for i in range(21)]
    landmarks[8] = (8, 640, 200)  # only index up
    # first move
    action, params1 = controller.process(landmarks, frame_shape)
    assert action == "MOVE"

    action, params2 = controller.process(landmarks, frame_shape)
    assert params2["x"] == params1["x"]
