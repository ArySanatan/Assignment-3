'''4. Python program to find all armstrong numbers from 1 to 1000.'''
#important

def num_of_digits(num):
    num_of=0

    while(num!=0):
        num=num//10
        num_of +=1
    
    return num_of


def armstrong(num):
    arms = 0
    p=num_of_digits(num)
    while(num!=0):
        remainder=num%10
        arms = pow(remainder,p) + arms
        num=num/10
        
    return arms
    
    

for i in range(1,1001):
    arms = 0
    p=num_of_digits(i)
    while(i!=0):
        remainder=i%10
        arms = pow(remainder,p) + arms
        i=i/10
        
    if (i==armstrong(i)):
        print(i)
    
