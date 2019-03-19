#file

#w mode will overwrite
#r read mode
#a append mode
f=open("C:/Users/Administrator/Downloads/boa.txt","w")
f.write("i am here \n")
f.write("you are there in a folder\n")
f.close()


f=open("C:/Users/Administrator/Downloads/boa.txt","r")
for line in f:
    print(line.rstrip())
f.close()
