#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *


def pyramid_1(n:int)->bool:

    for i in range(n):
        for k in range(n-1-i):
            print(' ',end='')
        for j in range(i+1):
            print("*",end=' ')
        print()

def pyramid_2(n:int)->None:

    for i in range(1,n+1):
        print(" "*(n-i)+"* "*(i))



try:
    n=int(input("enter n :"))
    if n<=0:
        print("Pattern cant be constructed")
    else:
        pyramid_2(n)
except:
    print("give integer only")