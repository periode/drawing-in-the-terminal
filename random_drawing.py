from sys import stdout
from time import sleep
import random

interval = 0.001

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

def random_drawing():
    while True:
        if random.random() > 0.5:
            spell("^", 0)
        else:
            spell(".", 0)



try:
    random_drawing()
except KeyboardInterrupt:
    print(term.normal+"bye!")
