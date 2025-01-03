'''4. Python program to find all armstrong numbers from 1 to 1000.'''
#solved - good logic buiding 

def num_of_digits(num):
    num_of=0

    while(num!=0):
        num=num//10
        num_of +=1
    
    return num_of
    
    
def armstrong(i):
    h=i
    armstrong = 0
    while (i != 0) :
        rem=i%10
        power=pow(rem,num_of_digits(h))
        armstrong = armstrong + power
        i=i//10
    
    return armstrong    
        
print("Armstrong Numbers from 1 to 1000 are ")        
for n in range(1,1001):
    if (n==armstrong(n)):print(n,end="   ") 

  