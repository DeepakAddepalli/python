import random
import time

tooHot = Exception("Over Temperature Limit","Check the water level")
maxtemp = 150
def get_temp():
    return random.randint(30,155)

while True:
    current_temp = get_temp()
    print(current_temp, end="")
    if  current_temp< maxtemp:
        print("Keep Driving")
        time.sleep(0.2)
    else:
        raise tooHot
