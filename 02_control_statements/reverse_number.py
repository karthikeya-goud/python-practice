def reverse_number(n:int)->int:
    t=0
    while n!=0:
        r=n%10
        t=t*10+r
        n=n//10
    return t


try:
    n=int(input("enter n:"))
    if n<0:
        n=n*-1
        print("Reverse number is ",-1*reverse_number(n))
    else:
        print("Reverse number is ",reverse_number(n))
except:
    print("enter integer only")