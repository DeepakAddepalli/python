import os

ipfile ="ip.txt"

f =open(ipfile,"r")

def myping(ip):
    return not os.system("ping -n 1 {} >NUL".format(ip))

for ip in f:
    ip =ip.strip()
    if myping(ip):
        print("{} is up".format(ip))
    else:
        print("{} is down".format(ip))