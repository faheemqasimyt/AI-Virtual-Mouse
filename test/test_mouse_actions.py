import pytest
from Function.mouse_actions import execute_action


def test_move_action(mocker):
    mock_move = mocker.patch("pyautogui.moveTo")
    params = {"x": 800, "y": 600}
    execute_action("MOVE", params)
    mock_move.assert_called_once_with(800, 600, duration=0.1)


def test_left_click(mocker):
    mock_click = mocker.patch("pyautogui.click")
    execute_action("LEFT_CLICK", {})
    mock_click.assert_called_once()


def test_right_click(mocker):
    mock_rclick = mocker.patch("pyautogui.rightClick")
    execute_action("RIGHT_CLICK", {})
    mock_rclick.assert_called_once()


def test_scroll(mocker):
    mock_scroll = mocker.patch("pyautogui.scroll")
    execute_action("SCROLL", {"delta": 40})
    mock_scroll.assert_called_once_with(40)


def test_no_action(mocker):
    mock_move = mocker.patch("pyautogui.moveTo")
    mock_click = mocker.patch("pyautogui.click")
    execute_action("NO_ACTION", {})
    mock_move.assert_not_called()
    mock_click.assert_not_called()
