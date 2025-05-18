def isLeapYear_1(year:int)->bool:

    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def isLeapYear_2(year:int)->bool:

    return (year%4==0 and year%100!=0) or year%400==0



try:
    year=int(input("Enter year: "))
    if year<0:
        print("year cant be negative")
    else:
        print(f"{year} is a "+("Leap Year" if isLeapYear_2(year) else "Not a Leap Year"))
except:
    print("Enter year correctly")