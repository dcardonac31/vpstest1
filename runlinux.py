import sys, string, os
import random
from time import sleep

while True:
    print("Run xmrig")
    os.startfile("./run.sh")
    number_ramdom = random.randint(300,900)
    print("Wait minutes: ",(number_ramdom/60))
    sleep(number_ramdom)
    print("Stop xmrig")
    os.startfile("./pkill.sh")
    number_ramdom = random.randint(300,1800)
    print("Wait minutes: ",(number_ramdom/60))
    sleep(number_ramdom)