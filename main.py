import pyautogui
import time
time.sleep(5)
c = 0
while c <= 10:
    pyautogui.typewrite('hello ' + str(c))
    pyautogui.press("enter")
    c += 1
    time.sleep(1)
