

def sum_1(lst:list[float])->float:
    s=0
    for ele in lst:
        s+=ele
    return s

try:
    lst=[float(x) for x in input("enter n numbers by giving space :").split()]
    print(f"Sum is {sum_1(lst)}")
except:
    print("enter numbers correctly")