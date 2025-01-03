'''10. Write a Python program to get the smallest number from a list without using any builtin
function.'''
#solved - sorting

list=[45,25,36,84,1,254,789,9,56,85,-1,23,78]


n=0
while(n<len(list)-1):
        if list[n] < list[n+1]: 
            c=list[n]
            list[n]=list[n+1]
            list[n+1] = c
        n+=1
    

print("Smallest Number from the list is ",list[-1])