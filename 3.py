'''3. Python program to print all prime numbers from 1 to 100.'''

#very good logic

print("All Prime Numbers from 1 to 100 are : ")
n=2

while(n<=100):
    k=2
    for i in range (1,n+1):
        if (n%i !=0 and n%1==0): 
            k=k+1
            
    if (n==k):print(n,end="  ")        
    n+=1
       