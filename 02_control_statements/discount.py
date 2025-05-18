
# if amt < 500            0% discount
# if amt in [500,1999.99]    5%
# if amt in [2000,4999.99]   10%
# if amt >5000            15%


def bill(amt:float)->float:
    dis=0.0
    if 500<=amt<2000:
        dis=amt*0.05
    elif 2000<=amt<5000:
        dis=amt*0.1
    else:
        dis=amt*0.15
    return dis

try:
    amt=float(input("enter total amoubnt:"))
    if amt<=0:
        print("Amount cant be <=0")
    else:
        print(f"Discounted Amount:{(dis:=bill(amt)):.2f}")
        print(f"Amount Payable: {amt-dis:.2f}")
except:
    print("Enter Amount Correctly")
