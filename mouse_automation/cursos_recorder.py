#!/usr/bin/python3

"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""

from  pynput import mouse
import sys
from datetime import datetime

#Records mouse movements

click_counter = 0
click_report = [f">{datetime.now()}:\n"]
def onclick(x,y, button, pressed):
    global click_counter

    #avoid double report during press and release
    if(pressed == False):
        click_counter+=1
        out = f"{str(datetime.now())[:21]}: {button} clicked ({x}, {y}) #{click_counter}\n"
        click_report.append(out)
        print(out)



#################################
print("Mouse Recording Initiated")
print("To end recording press ctr + c")
try:
    #Create a listener for the mouse
    with mouse.Listener(
        on_click = onclick #bind call back
    ) as listener:
        listener.join()
except KeyboardInterrupt as e:
   print()
   print("Terminated")
   click_report.append("-- --\n")
   with open("click_report.txt", "+a") as out:
       out.writelines(click_report)
   sys.exit(0)
    