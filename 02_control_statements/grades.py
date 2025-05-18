class MarksError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def grade(marks:int)->str:

    match marks:
        case marks if marks>89:
            return "O"
        case marks if marks>79:
            return "A+"
        case marks if marks>69:
            return "A"
        case marks if marks>59:
            return "B+"
        case marks if marks>49:
            return "B"
        case marks if marks>39:
            return "C"
        case _:
            return "F"


try:
    marks=int(input("enter integer marks :"))
    if marks>100:
        raise MarksError("Marks should be <=100 only")
    if marks<0:
        raise MarksError("Marks should be >=0 only")
    print(f"Student grade is {grade(marks)}")
except MarksError as e:
    print(e)
except:
    print("enter marks in integer format only")
        