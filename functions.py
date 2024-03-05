'''Store your functions here'''


def help_(function:str) -> None :
    '''Prints the given function's repr'''
    try:
        doc = func_dict[function].__doc__
        print(doc if doc else "No documentation provided for given function")

    except KeyError:
        print("No such util. run '$python3 cliutils.py list' to get a list of available utils")

def list_functs(args) -> None:
    '''Prints a list of available functions. usage: '$python3 cliutils.py list'. Flags: -m for printing function repr with it.'''
    
    if args == "-m":
        
        for key in func_dict:
            print(f"{key}: {func_dict[key].__doc__}")

    else:
        print("\n".join([key for key in func_dict]).lstrip("\n"))

#Example functions
#Make sure function accepts only one str parameter

def upp(val:str) -> None :
    '''Converts to uppercase. usage: $python3 cliutils.py upper <Text here>'''
    
    res = ""

    for i in val:
        res += i.upper() if "a" < i < "z" else i

    print(res)

def lowe(val: str) -> None:
    '''Converts to lowercase. usage: $python3 cliutils.py lower <Text here>'''
        
    res = ""

    for i in val:
        res += i.lower() if "A" < i < "Z" else i

    print(res)

def invert(val: str) -> None:
    '''Inverts input, usage : `$python3 cliutils.py invert <Text here>'''
    print(val[::-1])



#Add your function to the dict
func_dict = {
    "help":help_,
    "upper":upp,
    "lower":lowe,
    "list":list_functs,
    "invert":invert
    }

