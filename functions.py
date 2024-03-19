'''Store your functions here'''
from random import choice



#Example functions
#Make sure function accepts only one list parameter

def upp(args) -> None :
    '''Converts to uppercase. usage: $python3 cliutils.py upper "<Text here>"'''
    
    res = ""

    for i in args[0]:
        res += i.upper() if "a" <= i <= "z" else i

    print(res)

def lowe(args) -> None:
    '''Converts to lowercase. usage: $python3 cliutils.py lower "<Text here>"'''
        
    res = ""

    for i in args[0]:
        res += i.lower() if "A" <= i <= "Z" else i

    print(res)

def invert(args) -> None:
    '''Inverts input, usage : `$python3 cliutils.py invert "<Text here>"'''
    print(args[0][::-1])

def randomcase(args):
    '''converts input to randomcase. usage: `$python3 cliutils.py randomcase "<text here>"`'''

    print(''.join(choice((str.upper, str.lower))(char) for char in args[0]))

    


#Add your function to the dict
func_dict = {
    "upper":upp,
    "lower":lowe,
    "invert":invert,
    "randomcase":randomcase
    }
