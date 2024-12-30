'''1. Python program to calculate the sum of all the odd numbers within the given range'''

print("Enter Range (a:b)")
a=int(input("a : "))
b=int(input("b : "))

sum=0
for r in range(a,b+1):
    if (r%2!=0):
        sum = sum + r

print("Sum of all odd digits in given range : ",sum)