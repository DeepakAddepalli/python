from datetime import datetime
import time

now = datetime.now()
today = datetime.today()

print(now)
print(now.astimezone())
print(today)
print(today.ctime())

start = time.time()

print(time.ctime(start))

for x in range(1000000):
    y=x*x
end = time.time()
print(time.ctime(end))
print(end-start)

time.sleep(1)
print("Done")