

import math

p=[]
e=[]

#prompt for input number
print("input number to factorize")
inputNumber = int(input())

print("")
print("working on "+ str(inputNumber))

for n in range(2, 1 + math.floor(math.sqrt(float(inputNumber)))):
	
