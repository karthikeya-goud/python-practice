def checkEven_1(n:int)->bool:
    return n%2==0

def checkEven_2(n:int)->bool:
    return n&1==0

print("Check number is even or odd")
try:
    n=int(input("enter a integer :"))
    print(("Even" if checkEven_2(n) else "Odd")+" Number")
except:
    print("Enter integer only next time")