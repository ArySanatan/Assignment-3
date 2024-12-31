'''4. Python program to find all armstrong numbers from 1 to 1000.'''
#not solved - problem in logic buiding 

def num_of_digits(num):
    num_of=0

    while(num!=0):
        num=num//10
        num_of +=1
    
    return num_of
    
sum=0
i=1
while(i<=1000):
    n=0
    while(n<=num_of_digits(i)):
        remainder = i % 10
        sum=sum+pow(remainder,num_of_digits(i))
        n=n+1
        
    if (i==sum): print(i)
    i=i+1
        

