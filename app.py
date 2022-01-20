import pyautogui
import time
pyautogui.FAILSAFE = False
count = int(input("Enter the write number : "))
sleep = float(input("Enter time : "))
message = input("Please enter the message : ")

for i in range(0,count):
    time.sleep(sleep)
    pyautogui.typewrite(message)
    time.sleep(sleep)
    pyautogui.press("enter")