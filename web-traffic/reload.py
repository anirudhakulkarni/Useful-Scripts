import time
import pyautogui
time.sleep(5)
for i in range(100):
    pyautogui.hotkey("ctrlleft", "r") 
    time.sleep(0.4)
    print(i)