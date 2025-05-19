def pascal_triangle(n:int)->None:

    for i in range(n):
        print(" "*(n-i),end=' ')
        for j in range(i+1):
            if j==0:
                k=1
            else:
                k=k*(i-j+1)//j
            print(f"{k:3d}",end=' ')
        print()


try:
    n=int(input("Enter n:"))
    if n<=0:
        print("Pattern cant be created")
    else:
        pascal_triangle(n)
except:
    print("enter integer only")
