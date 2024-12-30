'''5. Find the sum of the series upto n terms
2 + 22 + 222 + 2222 + 22222 + ......
example:2 + 22 + 222 + 2222 + 22222 = 24690'''
#moderate

def terms(n):
    sum=0
    while(1<=n):
        sum = sum*10 + 2
        n=n-1
    return sum


n=int(input("Enter number of terms n : "))
sum=0

while (1<=n):
    sum = sum + terms(n)
    n=n-1
    
print("Sum of",n,"terms = ",sum)
    
    
