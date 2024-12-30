'''2. Python program to find the factorial of a given number.'''

num=int(input("Enter Number : "))
i=1
factorial=1
while(i<=num):
    factorial=factorial*i
    i=i+1

print("Factorial of",num,"=",factorial) 