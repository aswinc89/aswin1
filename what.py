import pyautogui as pt
import time

l=int(input("Enter the limit:"))
m=input("Enter the msg:")
i=0
time.sleep(3)
for i in range(l):
    pt.typewrite(m)
    pt.press("enter")