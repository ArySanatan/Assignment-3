'''10. Write a Python program to get the smallest number from a list without using any builtin
function.'''
##not solved - problem in logic buiding

list=[45,25,36,84,1,254,789,9,56,85,23,78]


n=0
i=0
while(n<=(len(list)-1)):
    freeze=list[n]
    
    while(i<=(len(list)-1)):
        checker=list[i]
        if (freeze>checker): list.remove(freeze)
        else: list.remove(checker)
        i=i+1
    n=n+1
print(list)