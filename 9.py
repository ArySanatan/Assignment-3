'''9. Write a Python program to multiply all the items in a list.'''

list = [2,2,2,2,3,6]

i=0
multiply=1
while(i<=len(list)-1):
    multiply = list[i] * multiply
    i=i+1

print("Multiplication of all items = ",multiply)