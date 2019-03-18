fib =[0,1]
while sum(fib[len(fib)-2:]) <= 1000 :
    fib.append(sum(fib[len(fib)-2:]))
print(fib)




def getindices(word,char):
    indices=[]
    for x in range(len(word)):
        if word[x]== char:
           indices.append(x)
    return indices
           
print (getindices("banana","a"))
