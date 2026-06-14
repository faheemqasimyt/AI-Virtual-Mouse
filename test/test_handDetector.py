import pytest
import numpy as np
import cv2
from unittest.mock import MagicMock, patch
from Function.handDetector import HandDetector


#avoid needing the real model
class FakeHandLandmarker:
    def detect(self, mp_image):
        return None


@pytest.fixture
def detector():
    with patch(
        "mediapipe.tasks.python.vision.HandLandmarker.create_from_options",
        return_value=FakeHandLandmarker(),
    ):
        det = HandDetector(model_path="dummy.task")
    return det


def test_initialization():
    # Test that detector can be created (mock will prevent actual model loading)
    with patch("mediapipe.tasks.python.vision.HandLandmarker.create_from_options"):
        det = HandDetector(model_path="fake.task")
    assert det.detector is not None


def test_get_landmark_positions_no_hand(detector):
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    detector.results = MagicMock(hand_landmarks=None)
    landmarks = detector.get_landmark_positions(img)
    assert landmarks == []


def test_get_landmark_positions_with_hand(detector):

    mock_hand = MagicMock()

    mock_landmarks = [MagicMock(x=0.5, y=0.5) for _ in range(21)]

    mock_landmarks[8] = MagicMock(x=0.75, y=0.25)
    mock_hand.__iter__.return_value = iter(mock_landmarks)
    mock_hand.__len__.return_value = 21
    mock_hand.__getitem__.side_effect = lambda idx: mock_landmarks[idx]

    detector.results = MagicMock(hand_landmarks=[mock_hand])
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    landmarks = detector.get_landmark_positions(img)
    assert len(landmarks) == 21

    assert landmarks[8] == (8, 480, 120)
