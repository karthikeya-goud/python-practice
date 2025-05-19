def gcd(a:int,b:int)->int:

    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

try:
    lst=[int(x) for x in input("enter whole numbers :").split()]
    for i in lst:
        if i<0:
            print("enter whole numbers only")
            break
    else:
        if len(lst)==0:
            print("No number given")
        elif len(lst)==1:
            print("Given only one number : ",lst[0])
        elif len(lst)==2:
            print(f"Gcd is : {gcd(lst[0],lst[1])}")
        else:
            res=gcd(lst[0],lst[1])
            for i in range(len(lst)-2):
                res=gcd(res,lst[2+i])
            print("Gcd is :",res)
except:
    print("enter integers only")