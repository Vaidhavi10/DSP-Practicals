#program 1
import math 
num = 9

print ("Square root :" , math.sqrt(num))
print ("Factorial:" , math.factorial(4))
print("Power :", math.pow(3,3))
print("Log:", math.log(2))

#program 2

from functools import reduce
numbers = [6,7,8,9,10]

result = reduce(lambda x,y: x+y , numbers)
print("Sum using :",result)

#program 3

def sub(a,b):
    return a-b
def divide(a,b):
    return a/b

import my_module 
print("Substraction:", my_module.sub(5,3))
print("Division:", my_module.divide(4,2))
    