#!/usr/bin/python3

"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""
import pyautogui
import time



avgsleep = 2.5 #seconds


""""
Intended Script

2024-04-06 14:57:52.5: Button.left clicked (1040.7158203125, 364.5535888671875) #1 #Arrow
2024-04-06 14:57:54.9: Button.left clicked (997.7490234375, 343.17059326171875) #2 Option
2024-04-06 14:57:56.6: Button.left clicked (1135.2607421875, 363.26629638671875) #3 Lookup
2024-04-06 14:58:01.5: Button.left clicked (1573.3875732421875, 140.77728271484375) #4 Download
2024-04-06 14:58:0 pyt5.3: Button.left clicked (1129.36083984375, 773.8822631835938) #5 Save
2024-04-06 14:58:07.8: Button.left clicked (173.04000854492188, 22.123916625976562) #6 Tab
---
2024-04-06 14:58:11.7: Button.left clicked (1040.4361572265625, 367.91607666015625) #7 Arrow
2024-04-06 14:58:13.6: Button.left clicked (1011.6156005859375, 390.0740661621094) #8 Option
2024-04-06 14:58:15.6: Button.left clicked (1106.247314453125, 356.12646484375) #9 Lookup
2024-04-06 14:58:18.6: Button.left clicked (1573.8199462890625, 140.72552490234375) #10 Download
2024-04-06 14:58:22.4: Button.left clicked (1148.9051513671875, 778.675537109375) #11 Save
2024-04-06 14:58:25.1: Button.left clicked (127.14289855957031, 23.540664672851562) #Tab
2024-04-06 14:58:36.8: Button.left clicked (1095.394287109375, 949.31640625) #13 Terminal
-- --


"""

class Target:
    def __init__(self, x,y, name = ""):
        self.x = x
        self.y = y
        self.name = name
    def click(self): 
        pyautogui.click(self.x, self.y)
   

arrow = Target(1040.60, 426.55, "Arrow")
lookup = Target(1135.25, 430.00, "Lookup")
download = Target(1573.5, 140.73, "Download")
save = Target(1130, 775.5, "Save")
x = Target(464.090576171875, 19.655288696289062, "Quit")
tab = Target(130.6, 22.5, "Tab")


targets = [arrow, lookup, download, save, x, tab]
option0 = Target(997.7490234375, 410.17059326171875)
optionYD = 42
time.sleep(10)
for c in range(23):
    option2click = Target(option0.x, option0.y + optionYD , f"Option({round(option0.x)}, {round( option0.y + optionYD)}) #{c}")
    targets.insert(1, option2click)
    sequence = ""
    for t in targets:
        sequence+= f" > {t.name}"
    print(f"c#{c}:  {sequence}")
    for t in targets:
        time.sleep(avgsleep-1)
        if t.name == "Save" or t.name == "Download":
            time.sleep(avgsleep-1) 
        if t.name == "Download":
             time.sleep(avgsleep) # sleeps twice the average
        t.click()
    targets.remove(option2click)
    for t in targets:
        sequence+= f" > {t.name}"
    print(f"c#{c} sequence")


    