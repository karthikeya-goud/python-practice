
def isUpper(ch:str)->bool:
    return ord(ch)<91 and ord(ch)>64

def isLower(ch:str)->bool:
    return 96<ord(ch)<123

def isDigit(ch:str)->bool:
    return 47<ord(ch)<58

try:
    ch=input("Enter any character from keyboard :")
    if len(ch)!=1:
        raise ValueError()
    if isUpper(ch):print("Upper Case is Entered")
    elif isLower(ch):print("Lower Case is Entered")
    elif isDigit(ch):print("Digit Case is Entered")
    else:print("special Character is Entered")
except:
    print("Enter Single character only")