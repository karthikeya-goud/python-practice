
def pyramid(n:int)->None:
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*(i))

def rev_pyramid(n:int)->None:
    for i in range(n,0,-1):
        print(" "+" "*(n-i)+"* "*(i))


try:
    n=int(input("enter n :"))
    if n<=0:
        print("pattern cant be construced give >0 integer")
    elif n&1==0:
        print("diamond pattern cant be construed with even nbumber")
    else:
        t=n//2
        pyramid(t+1)
        rev_pyramid(t)
except:
    print("give interger only")