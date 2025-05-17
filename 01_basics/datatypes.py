# data types are used to tell to the complier to allocate memory
# for the given type

# in python we have Scalar datatype and collection datatype

# Scalar Datatype : type which holds only single value
# Ex : int,float,complex,bool,Nonetype

# Collection Datatype: type which holds multiple value
# we can distingush them as
# 1. Sequesnce collection
#   Ex: str,list,tuple,range,bytes,bytearray
# 2. Sets
#   Ex: set,frozenset 
# 3. Mapping
#   Ex: dict


#==================================================================

# int type

# used to hold any integer value 
# in python we dont have limit for integer


a = 10 #10 is integer liter assigned to 'a' , so "a" is int type

a=111111111111111111111111111111111111111111111111111111111111111111111111 # can be any limit , but not recomended

a = 10_21_250 # we can use '_' for separtor for human understandability like 10,21,250 rs

# float type

# a variable said to be float if it has decimal in it it
# in pyhton we have limit to float data type we it exceds the limit to shows as 'inf' infinity

import sys
print(sys._float_info)

a = 10.
a = 10.34
a = 0.1e2
a= 2.1e-2

# we can use e pr E noation for exponetial "2.1e2"=> (2.1)*pow(10,2)


# complex data type

# python supports complex data type 
# it should be in form of a+bj

c1=3+2j
c2=0j
c3=3    #treats as int only



# boolean data type

# we have True,False note they are case sensitive

# used to for checking conditions

a=True
if a:
    print("True")


# None data type

# it is used when we need an empty conatiner to use
# it can also use to change address pointer to none so garbage collector can deallocate the unusedspacw


a=10
b=None
a=None