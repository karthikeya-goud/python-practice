from math import sqrt

def solve(a:int,b:int,c:int)->tuple[float,float] | str:
    if (eq1:=b*b)>(eq2:=4*a*c):
        r1=(-b+(eq3:=sqrt(eq1-eq2)))/(2*a)
        r2=(-b-eq3)/(2*a)
        return (r1,r2)
    elif eq1==eq2:
        r1=r2=(-b)/(2*a)
        return (r1,r2)
    else:
        return "Roots Are Imaginary"

try:
    a,b,c,*d=[int(x) for x in input("enter a b c values: ").split()]
    if len(d)>=1:
        print("Enter a b c values only")
    else:
        res = solve(a,b,c)
        if type(res)==tuple:
            print(f"roots are \nr1={res[0]}\nr2={res[1]}")
        else:
            print(res)
except:
    print("Enter a,b,c values correctly")