#!/usr/bin/python
'''

Progress Bar Module

@Author: Leonardo Duarte
@Methods:
    ProgressBar(current : float, total : float= 100.0, ...) -> float
    Calculate current progress and display bar

@Variables:
    PROG_CHAR : str - Progress indication char      | Default: '█'
    PEND_CHAR : str - Pending indication char       | Default: ' '
    BAR_LEN   : int - Prog bar length in n° chars   | Default: 10

@Exceptions:
    Invalid progress display request: Raised when user tries to ask for a progress bar
                                      but the current percentage is not with 0 and 100 percent


Copyright (c) 2023 Leonardo Duarte

'''

import math
import time
import cursor



_total = 10
_default_prog_char = "‒" # "█" '⸺' 
_default_pend_char = ' ' # " "
          #0,1,2,3,4,5,6,7
_emojis = "🍺🥃🏃🏻🤟🏼👾💀🎃🤖☄️"


PROG_CHAR = _default_prog_char# _emojis[7] #_default_prog_char
PEND_CHAR = _default_pend_char
BAR_LEN = 18

def ProgressBar(current : float, total : float= 100.0, 
                label   : str  = "" , etc : float = -1.0, 
                isoit : str  ="", color = None) -> float:
   
    """
    Calculate current progress and display bar \n
    @params:
        current [in]: current progress\n
        total [in] : total target value [o]\n
        label [in] : progress bar label [o]\n
        etc   [in] : estimated time to completion (minutes  [o]\n
        init_ascci_time [in]:  init_ascci_time [o] \n
        [o] => Optional
    """
    line_length = BAR_LEN
    progress_char = PROG_CHAR
    pendding_char = PEND_CHAR
    """Progres Bar Lenght in chars"""
    current_progress = current / total
    if current_progress > 1 or current_progress < 0:
        raise Exception(f" Invalid progress display request. c: {current},  total:  {current} percen: {current_progress*100}%") 
    complete_c = math.floor(line_length * current_progress)
    """ char count complete """
    pending_c = line_length -complete_c
    """ char count pending """
    cbar = ''
    #if colorama available 
    try:
        import colorama
        setcolor = colorama.Fore.BLUE  if color != None or type(color) != type (colorama.Fore.BLUE) else color
        resetall = colorama.Style.RESET_ALL
        cbar =  f" {setcolor}{progress_char*complete_c}{pendding_char*pending_c} {resetall} | {int(current_progress*100)}%" 
    except:
        cbar = f"|{progress_char*complete_c}{pendding_char*pending_c}|{int(current_progress*100)}%"

    #add label in the beging
    if type(label) == str and label != "":
        cbar = label + cbar 

    
    #Add init asscii time
    if type(isoit) == str and isoit != "":
        cbar = cbar + f" IT: {isoit}"

    #Convert etc to float if it is an int
    etc = float(etc) if type(etc) == int else etc 
    #add ETC at the end
    if type(etc) == float and etc != -1.0:
        #m minutes
        cbar = cbar + f" ETC:{round(etc,2)}m"
 
    print(f"\r {cbar}", end='\r')
    time.sleep(0.01)
    return current_progress

ProgressBar.__doc__= """
    Calculate current progress and display bar \n
    @params:
        current [in]: current progress\n
        total [in] : total target value [o]\n
        label [in] : progress bar label [o]\n
        etc   [in] : estimated time to completion (minutes  [o]\n
        init_ascci_time [in]:  init_ascci_time [o] \n
        [o] => Optional
    """


if __name__ == "__main__":
    for i in range(_total):
        cursor.hide()
        ProgressBar(i, _total, label=f"{_emojis[7]}")
        time.sleep(1)
    help(ProgressBar)
    print("test completed")