'''6. Write a Python function to check whether a number falls in a given range.'''

def fall_in_range(n1,n2):
    num=int(input("Enter a Number : "))
    
    if (n1<n2):
        if (num>=n1 and num<=n2):
            print(num,"is in the range of ",n1,"and",n2)
        else: print("Not  in given range")
    else: print("Invalid Range")

print("Enter Range [a,b]")
fall_in_range(int(input("a = ")),int(input("b = ")))