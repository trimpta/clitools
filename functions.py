'''Store your functions here'''
from random import choice


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

#Example functions
#Make sure function accepts only one str parameter

def upp(args) -> None :
    '''Converts to uppercase. usage: $python3 cliutils.py upper "<Text here>"'''
    
    res = ""

    for i in args[0]:
        res += i.upper() if "a" < i < "z" else i

    print(res)

def lowe(args) -> None:
    '''Converts to lowercase. usage: $python3 cliutils.py lower "<Text here>"'''
        
    res = ""

    for i in args[0]:
        res += i.lower() if "A" < i < "Z" else i

    print(res)

def invert(args) -> None:
    '''Inverts input, usage : `$python3 cliutils.py invert "<Text here>"'''
    print(args[0][::-1])

def randomcase(args):
    '''converts input to randomcase. usage: `$python3 cliutils.py randomcase "<text here>"`'''

    print(''.join(choice((str.upper, str.lower))(char) for char in args[0]))

    


#Add your function to the dict
func_dict = {
    "help":help_,
    "-m": _m,
    "upper":upp,
    "lower":lowe,
    "list":list_functs,
    "invert":invert,
    "randomcase":randomcase
    }

