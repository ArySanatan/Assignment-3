'''8. Write a Python function to find the Max of three numbers.'''

def maxofthree(a,b,c):
    if (a>b and a>c): return a
    elif (b>c and b>a): return b
    else : return c
    
a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))

largest=maxofthree(a,b,c)
print(largest, "is Largest of three")