'''11. Write a Python program to find the list of words that are longer than n from a given list of
words. (n is an integer input)'''
##important - good logic build

n=int(input("Enter n : "))
list=["Good","Bad","Mango","run","Write","a","Python","program","to","find","the","list","of","words","that","are","longerthan","fromagivenlist","ofwords"]

i=len(list)-1

while(0<=i):
    char_in_one_element=len(list[i])
    if (char_in_one_element<=n): 
        list.remove(list[i])
        
    i=i-1 

print(list)