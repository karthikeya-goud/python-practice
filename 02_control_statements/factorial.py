def fact(n:int)->int | str:
    if n<0:
        return "Cant Do factorial of -ve numbers"
    if n==1 or n==0:
        return 1
    f=1
    for i in range(2,n+1):
        f=f*i
    return f


try:
    n=int(input("enter n:"))
    res=fact(n)
    if type(res)==str:
        print(res)
    else:
        print(f"result : {res}")
except:
    print("Enter Integers only")