def fib(n:int)->list[int]:
    a,b=0,1
    res=[]
    for i in range(n):
        res.append(a)
        a,b=b,a+b
    return res

try:
    n=int(input("enter n :"))
    if n<=0:
        print(f"No series can be generated for this value {n}")
    else:
        print(f"Series is {fib(n)}")
except:
    print("Enter integer only")