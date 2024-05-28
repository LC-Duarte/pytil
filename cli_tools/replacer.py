

#!/usr/bin/python3
#Replacer.py
"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""

"""
Replace- replaces regex by value 
replaces regex in file by detrmined value and delivers the output in a new file
"""

import datetime
import os
import sys
import getopt

ARG_LIST = sys.argv[1:]


def printList(list, **kwargs):
    bullet = kwargs.get("bullet", True)
    tab = kwargs.get('tab', True)
    limit = kwargs.get('limit', -1)
    c = 0
    for x in list:
        out = ''
        if tab:
            out += '\t'
        if bullet:
            out += '* '
        out += x
        print(out)
        c += 1
        if c == limit:
            break

    

#\$P\{[A-Za-z][0-9]?.?[A-Z\-Z]*[0-9]?\}
def genFileName(**kwargs):
    px = kwargs.get("prefix", 'out')
    sx = kwargs.get("sulfix", None)
    typ = kwargs.get("type_mod", None)
    time_mod = kwargs.get("time_mod", False)
    
    ct = datetime.datetime.now()
    name_mod = f'{ct.month}{ct.day}{ct.hour}{ct.minute}{ct.second}'
    
    name = px
    if sx != None:
        name += sx
    if time_mod:
        name += name_mod
    if typ != None: 
        name += typ
    return name


OUT_TYPE = '.txt'
OUT_PX = 'gu'

CONTENT  =''

REGEX_SUGESTIONS =  ["\$P\{[A-Za-z][0-9]?.?[A-Z\-Z]*[0-9]?\}"]

# OPT
OPT = "r:i:o:"
# Long OPT
LONG_OPT = ["re", "input", "output"] 
NO_PARAM = 'N~'

def get_pattern(target):
    try:
        with open(target ) as pattern_file:
            data = [tuple(line.split()) for line in pattern_file]
            return data
    except Exception as e:
        print(str(e))

def get_input(target):
    content = ''
    try:
        with open (target, 'r') as in_file:
            content = in_file.read()
        return content
    except Exception as e:
        print(str(e))
def print_result(result, target):
    try:
        with open(target, 'w') as out_file:
            out_file.write(result)
    except Exception as e:
        print(str(e))
    
        

def main():
    exc_path = os.getcwd()
    target_pattern = NO_PARAM
    target_input = NO_PARAM
    target_output = NO_PARAM
    try:
        
        # Parsing argument
        arguments, values = getopt.getopt(ARG_LIST, OPT, LONG_OPT)
        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-r", "--re") :
                target_pattern = currentValue
            elif currentArgument in ("-i", "-input"):
                target_input = currentValue
            elif currentArgument in ("-o", "--output"):
                target_output = currentValue
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
    print("** REPARAM **")
    if target_pattern == NO_PARAM:
        print("> Pattern file sugestions:")
        files = os.listdir(exc_path)
        printList(files, bullet = True, limit = 10)
        target_pattern  = input("Provide target pattern file: ")
    
    if target_input == NO_PARAM:
        files = os.listdir(exc_path)
        print("> Input file sugestions:")
        printList(files, bullet = True, limit = 10)
        target_input = input("Provide target file: ")
    if target_output == NO_PARAM:
        target_output  = genFileName(prefix=OUT_PX, type_mod = OUT_TYPE, time_mod = True)

    pattern_tuples = get_pattern(target_pattern)
    working_data = get_input(target_input)
    for k, v in pattern_tuples:
        working_data = working_data.replace(k, v)
    print_result(working_data, target_output)
    print("Finished")
if __name__ == "__main__":
    main()




