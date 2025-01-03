'''7. Write a Python function to check whether a number is perfect or not.'''

#Solved :]

def isperfect(num):
    i=1
    sum=0
    while (i<num):
        if (num%i==0):
            sum = sum + i
        i+=1
    
    if (num==sum): 
        print(f"{num} is Perfect Number")
    else:
        print("Not a Perfect Number")
        
    return sum

num = int(input("Enter Number : "))
isperfect(num)
