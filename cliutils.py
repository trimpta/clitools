#!/usr/bin/env python3
#22:24 05/03/2024
#Auther: Trimpta
#File: cliutils.py

'''
Cliutils
'''

import sys
from functions import *

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



if __name__ == "__main__":

    handle_args()
 