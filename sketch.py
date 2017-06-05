import time
import random
import noise
import blessings
import sys

import blessings

term = blessings.Terminal()

width = term.width
height = term.height

while True:
    #if random.random() > 0.1:
    #    for i in range (0, width):
    #        print("|", end="")
    #else:
    #    for i in range(0, width):
    #        print("_", end="")
    #sys.stdout.flush()
    #sleep(0.05)
    for i in range(0, width):
        if noise.pnoise2(i*0.9, time.clock()) > 0.4:
            print("'", end="")
        else:
            print(" ", end="")
        sys.stdout.flush()
        time.sleep(0.001)
