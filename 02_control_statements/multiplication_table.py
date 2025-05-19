def mul_table(n:int)->None:
    for i in range(1,11):
        print(f"{n:3d} x {i:2d} = {n*i:4d}")

try:
    n=int(input("enter number :"))
    mul_table(n)
except:
    print("enter interger number only")