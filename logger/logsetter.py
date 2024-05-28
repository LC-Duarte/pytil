#logsetter.py
"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""

import logging 
#Logging levels
INFO     = logging.INFO
DEBUG    =  logging.DEBUG
WARNING  = logging.WARNING
ERROR    = logging.ERROR
def setup(name, log_file = None,  log_level=INFO):
    """
    Set up a logger with the specified name and optional log file and log level.

    Args:
        name (str): The name of the logger.
        log_file (str, optional): The path to the log file. Defaults to None.
        log_level (int, optional): The log level. Defaults to logging.INFO.

    Returns:
        logging.Logger: The configured logger.

    Raises:
        None

    Examples:
        >>> logger = setup('my_logger', 'logs/log.txt', logging.DEBUG)
        >>> logger.info('This is an info message')
        >>> logger.error('This is an error message')
    """
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s-%(lineno)d: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    if log_file != None and type(log_file) == str :
        log_file = log_file+".log"
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

def dashed_line():
    log = logging.getLogger('main')
    line = "----------------------------------------"
    log.debug(line)

def print_objects(**kwargs):
    log = logging.getLogger('main')
    for k, v in kwargs.items():
        log.debug(f'{k}:')
        log.debug(f'{v}')
        dashed_line()

        
def print_list(list, **kwargs):
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
