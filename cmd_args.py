from sys import argv

filename=argv[1]
print(len(open(filename).readlines()))
