import pyautogui

last_position = None
while True:
    if last_position != pyautogui.position():
        last_position = pyautogui.position()
        print(pyautogui.position())