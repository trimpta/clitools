#!/usr/bin/env python3
#22:24 05/03/2024
#Auther: Trimpta
#File: cliutils.py

'''
Cliutils
'''

import sys
from functions import *


def help_(args) -> None :
    '''Prints the given function's repr'''
    try:
        doc = func_dict[args[0]].__doc__
        print(doc if doc else "No documentation provided for given function")

    except IndexError:
        print("Please provide util name. run '$python3 cliutils.py list' to get a list of available utils")

    except KeyError:
        print("No such util. run '$python3 cliutils.py list' to get a list of available utils")

def list_functs(args) -> None:
    '''Prints a list of available functions. usage: '$python3 cliutils.py list'. Flags: -m for printing function repr with it.'''
    
    if "-m" in args:
        
        for key in func_dict:
            print(f"{key}: {func_dict[key].__doc__}")

    else:
        print("\n".join([key for key in func_dict]).lstrip("\n"))

def _m(args) -> None:
    '''Prints -m help page'''
    raise NotImplementedError("Sucks to suck ill implement this later :>")


def handle_args() -> None:
    '''insert doc later'''

    # no functions
    if len(sys.argv) == 1:
        print("Please enter util name.")
        return
    
    program, func, *func_args = sys.argv

    try:
        func_dict[func](func_args)

    except KeyError:
        print("No such util. run '$python3 cliutils.py list' to get a list of available utils")
        return
    
    except IndexError:
        print("Please provide proper arguments.")
        return

inbuilt_utils = {
    "help":help_,
    "list":list_functs,
    "-m": _m,
}

func_dict.update(inbuilt_utils)

if __name__ == "__main__":

    handle_args()
 