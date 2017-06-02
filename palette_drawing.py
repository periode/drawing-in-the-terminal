# builtin packages
from sys import stdout
from time import sleep
import random

#additional packages > install using pip install <NAMEOFPACKAGE>
import noise
from blessings import Terminal

interval = 0.001

term = Terminal()
width = term.width
height = term.height

#helper function
#credit due to Adam Luchjenbroers on StackOverflow <3
def map(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#helper function to print one character at a time if you're on python2.x
def spell(string, line_break):
    index = 0

    while index < len(string):
        stdout.write(string[index])
        stdout.flush()
        sleep(interval)
        index += 1

    for x in range (0, line_break):
        print(" ")



def palette_drawing():

    while True:
        for x in range(0, width-2):
            col = map(x, 0, width-2, 0, 15)
            print(term.color(int(col))+"/", end="")
            stdout.flush()
            sleep(0.0001)


try:
    palette_drawing()
except KeyboardInterrupt:
    print(term.normal+"bye!")
