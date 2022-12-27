import pyautogui
import time
x = input("enter the string:")
c = int(input("enter the count:"))
n = 1
inDelay = int(input("enter the initial delay:"))
delay = int(input("enter the delay:"))
time.sleep(inDelay)
while n <= c:
    pyautogui.typewrite(x + " " + str(n))
    pyautogui.press("enter")
    n += 1
    time.sleep(delay)
