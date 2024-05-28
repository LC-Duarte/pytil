"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""
import logging 
def dashed_line():
    """
    Print a dashed line in the debug log.

    This function retrieves the main logger and logs a dashed line using the debug level.
    The dashed line is a string consisting of 50 hyphens.

    Parameters:
        None

    Returns:
        None
    """
    log = logging.getLogger('main')
    line = "----------------------------------------"
    log.debug(line)

def print_objects(**kwargs):
    """
    Print the key-value pairs of the given keyword arguments in the debug log.

    This function retrieves the main logger and iterates over the keyword arguments.
    For each key-value pair, it logs the key and value using the debug level.
    After logging each pair, it calls the `dashed_line()` function to print a dashed line in the log.

    Parameters:
        **kwargs (dict): The keyword arguments to be printed.

    Returns:
        None
    """
    log = logging.getLogger('main')
    for k, v in kwargs.items():
        log.debug(f'{k}:')
        log.debug(f'{v}')
        dashed_line()

        
def print_list(list, **kwargs):
    """
    Print a list in the debug log.

    This function takes a list of items and prints them in the debug log. It accepts optional keyword arguments to customize the printing behavior.

    Parameters:
        list (list): The list of items to be printed.
        **kwargs (dict): Optional keyword arguments.
            bullet (bool): Whether to prefix each item with a bullet point. Defaults to True.
            tab (bool): Whether to add a tab before each item. Defaults to True.
            limit (int): The maximum number of items to print. Defaults to -1 (print all items).
            name (str): An optional name to prefix the list with. Defaults to None.

    Returns:
        None
    """
    log = logging.getLogger('main')
    bullet = kwargs.get("bullet", True)
    tab = kwargs.get('tab', True)
    limit = kwargs.get('limit', -1)
    name = kwargs.get('name', None)
    c = 0
    if name != None:
        log.debug(f'{name}:')
    for x in list:
        out = ''
        if tab:
            out += '\t'
        if bullet:
            out += '* '
        out += x
        log.debug(out)
        c += 1
        if c == limit:
            break
    dashed_line()
