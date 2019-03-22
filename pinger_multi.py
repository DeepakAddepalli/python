import os,time
import queue
from threading  import Thread

q= queue.Queue()
ipfile ="ip.txt"

f =open(ipfile,"r")

for myip in f.readlines():
    q.put(myip.strip())
f.close()
def myping(ip):
    return not os.system("ping -n 1 {} >NUL".format(ip))

def worker():
    while not q.empty():
        ip = q.get()
        if myping(ip):
            print("{} is up".format(ip))
        else:
            print("{} is down".format(ip))

threads =[]

for x in range(25):
    threads.append(Thread(target=worker))

for t in threads:
    t.start()

start = time.time()
for t in threads:
    t.join()
end = time.time()

print(end-start)