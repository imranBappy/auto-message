import pyautogui
import time
import random

pyautogui.FAILSAFE = False
count = int(input("Enter the write number : "))
sleep = float(input("Enter time : "))
messages = input("Please enter the message Hi, Hello : ").split(",")
for i in range(0,count):
    time.sleep(sleep)
    pyautogui.typewrite(messages[ random.randint(0, len(messages)-1)])
    time.sleep(sleep)
    pyautogui.press("enter")