import pyautogui

pyautogui.FAILSAFE = True

def execute_action(action, params):
    if action == "MOVE":
        x, y = params["x"], params["y"]
        pyautogui.moveTo(x, y, duration=0.1)
    elif action == "LEFT_CLICK":
        pyautogui.click()
    elif action == "RIGHT_CLICK":
        pyautogui.rightClick()
    elif action == "SCROLL":
        delta = params["delta"]
        pyautogui.scroll(delta)
