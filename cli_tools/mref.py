#!/usr/bin/python3
"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""
"""
mref - match regex in file 
list all unique matches af a regex in a file 
delivers the output in a text file
"""
import re
import os
import sys
import getopt, sys
import datetime

ARG_LIST = sys.argv[1:]


OUT_TYPE = '.txt'
OUT_PX = 'gu'

CONTENT  =''

REGEX_SUGESTIONS =  ["\$P\{[A-Za-z][0-9]?.?[A-Z\-Z]*[0-9]?\}"]

# OPT
OPT = "r:i:o:"
# Long OPT
LONG_OPT = ["re", "input", "output"] 
NO_PARAM = 'N~'



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



def list_matches(target_file, target_pattern, **kwargs):
    unique = kwargs.get("unique", False)  
    persist = kwargs.get("persist", False)
    sort =  kwargs.get('sort', True)
    set_out_name = kwargs.get("out_name", None)

    with open (target_file, 'r') as in_file:
        content = in_file.read().replace('\n', '')
        print(f'> Matching "{target_pattern}" on "{target_file}". Only unique values = {unique}. Persitant result = "{persist}"')
        matches =  re.findall(target_pattern, content)
        unique_matches = set(matches)
        print(f"Matches count {len(matches)}; Unique Matches count {len(unique_matches)}")
        if sort:
            matches = sorted(matches)
            unique_matches = sorted(unique_matches)
        if persist:
            print("> Persist ON")
            out_name = genFileName(prefix=OUT_PX, type_mod = OUT_TYPE, time_mod = True) if set_out_name == None else set_out_name
            with open(out_name, 'w') as out_file:
                if unique:
                    for ix in unique_matches:
                        out_file.write(f"{ix}\n")
                    return unique_matches, out_name
                else:
                    for ix in matches:
                        print(f"{ix}")
                        out_file.write(f"{ix}\n")
                    return matches, out_name

        if unique:
            return unique_matches, None
        else:
            return matches, None


def main():
    exc_path = os.getcwd()
    target_pattern = NO_PARAM
    target_file = NO_PARAM
    target_output = NO_PARAM
    try:
        # Parsing argument
        arguments, values = getopt.getopt(ARG_LIST, OPT, LONG_OPT)
        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-r", "--re") :
                target_pattern = currentValue
            elif currentArgument in ("-i", "-input"):
                target_file = currentValue
            elif currentArgument in ("-o", "--output"):
                target_output = currentValue
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    print("** REGEX FINDER **")
    print(f"> executing from {exc_path}")
    if target_pattern == NO_PARAM:
        print("> Regex sugestions:")
        printList(REGEX_SUGESTIONS)
        target_pattern = input("Provide target regex: ")
        if target_pattern == "":
            target_pattern = REGEX_SUGESTIONS[0]
    if target_file == NO_PARAM:
        files = os.listdir(exc_path)
        print("> Input file sugestions:")
        printList(files, bullet = True, limit = 10)
        target_file = input("Provide target file: ")

    unique_matches, out_name = list_matches(target_file, target_pattern, unique = True, persist = True, out_name= target_output)
    if out_name != None:
        print(f'> Output generated {out_name}')
    print("FINISHED")

if __name__ == "__main__":
    main()




