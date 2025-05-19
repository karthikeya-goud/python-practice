


def pattern1(n:int)->None:
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()


def pattern2_1(n:int)->None:
    # *
    # * *
    # * * *
    # * * * *
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=' ')
        print()

def pattern2_2(n:int)->None:
    for i in range(1,n+1):
        print("* "*(i))



def pattern3(n:int)->None:
    # 5
    # 5 4
    # 5 4 3
    # 5 4 3 2
    # 5 4 3 2 1

    for i in range(n,0,-1):
        for j in range(n,i-1,-1):
            print(j,end=' ')
        print()

def pattern4(n:int)->None:
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1

    for i in range(n):
        for j in range(1,n+1-i):
            print(j,end=' ')
        print()


def pattern5(n:int)->None:
    # 5 4 3 2 1
    # 5 4 3 2
    # 5 4 3
    # 5 4 
    # 5

    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(j,end=' ')
        print()


try:
    n=int(input("enter n value :"))
    if n<=0:
        print("patter cant be constructed")
    else:
        pattern5(n) #change with ur required pattern
except:
    print("enter integer only")