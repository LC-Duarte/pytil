#!/usr/bin/python3

"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""
import pyautogui
import time, sys
from datetime import datetime



#Pixel padding 
SCREEN_PADDING = 5 
#Cursor action interval in seconds
ACTION_INTERVAL = 20
#Program Duration (HH:MM:SS)
DURATION =  "03:30:00" 
CLICK_COUNTER=0


#Convert the duration string to secons
DURATION_SECS = sum(int(x) * 60 ** i for i, x in enumerate(reversed(DURATION.split(':'))))


def dyn_msg(txt):
    #Prints message on the same line (without generating new output lines)
    sys.stdout.write(txt+ chr(13))
    sys.stdout.flush()

def click(): 
    pos = {'x':1619, 'y' :734}
    pyautogui.click(pos['x'], pos['y'])
    pyautogui.drag(10,0, 1, button="left")
    pyautogui.click(pos['x']+10, pos['y'])
    global CLICK_COUNTER
    CLICK_COUNTER +=1
    return pos


def countdown_timer(countdownto, disp = True):
    """
    CountDown Timer 
    countdownto specifies time to count down from
    disp specifies if the timer should be displayed in the cli

    """
    for sec in range(countdownto):
         m = "%2d" % (countdownto-sec)
         if disp:
             dyn_msg(m)
         time.sleep(1)

def main():
    global CLICK_COUNTER
    print(pyautogui.size())
    countdownto = 15  
    print(f"Cursor movment will begin in {countdownto} secconds")
    print(f"Place the cursor in the desired initial position")
    countdown_timer(countdownto)
    dateTimeObj = datetime.now()
#    print(f"{dateTimeObj} -- cliking @ {pos}"
    pos = pyautogui.position()
    start_time = time.time()
    curr_time = start_time
    max_time = start_time+DURATION_SECS
    print(f"{dateTimeObj} -- Staring execution @ {pos} until {datetime.fromtimestamp(max_time)}")
    i = 0
    while(curr_time < max_time):
        pos = click()
        dateTimeObj = datetime.now()
        out = f"{dateTimeObj} - Clicker automation is in execution - CurrentPos: ({pos['x']},{pos['y']}), ClickCounter: {CLICK_COUNTER}, Until: {datetime.fromtimestamp(max_time)} "
        dyn_msg(out)
        #apply interval between actions
        time.sleep(ACTION_INTERVAL)
        #update counter and time
        i +=1
        curr_time = time.time()
    #execution finshed
    print()
    print("Clicker automation is terminated. {CLICK_COUNTER} clicks performed")

if __name__ == "__main__":
    main()
