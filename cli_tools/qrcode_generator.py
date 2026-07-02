#!/usr/bin/python3

"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1

This tool generates qr code based on cli arguments
"""

import sys
import getopt #CLI Argument parsing

import segno #QRCode generation


long_options = ["help", "target=", "output="]
short_options = "ht:o:"


SCALE=5
BORDER=0

def generate_QR(target_string, output_path):
    """
    Generates QR code for target_string and saves it to output_path
    """

    qrcode = segno.make_qr(target_string)

    qrcode.save(
    output_path,
    scale=SCALE,
    border=BORDER,
    )



output : str ="qrcode.png"
target_string : str = None


if __name__ == "__main__":
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, short_options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print (f""" 
**QR CODE GENERATOR**
    Usage:
        $python qrcode_generator.py -t <target_string> -o <output_path>
    Parameters
    -t|--target target_string -- Qr Code target string [recquired]
    -o|--output output_path -- Output path string [optional, default: {output} ]
    -h|--help -- Request help

    If you get a command not found error when setting a URL target, use "" around it
                    """)
                #terminate code after help
                sys.exit(0)
                
            elif currentArgument in ("-t", "--target"):
                target_string = currentValue
                print(f"target defined as: '{currentValue}'")

            elif currentArgument in ("-o", "--output"):
                output=currentValue
                print(f"Output path set to: '{output}'")
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    if target_string != None:
        generate_QR(target_string, output)