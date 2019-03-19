#csv


f=open("marks.csv","r")

for marks in f:  
    a = marks.rstrip().split(",")
    print(a[0].capitalize(),sum(map(int,a[1:])))
f.close()
