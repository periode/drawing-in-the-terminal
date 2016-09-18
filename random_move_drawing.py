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

def random_move_drawing():
    while True:
        with term.location(random.randint(0, width-2), random.randint(0, height)):
            if random.random() > 0.5:
                print(" ", end="")
            else:
                print("-", end="")
            term.location()


try:
    random_move_drawing()
except KeyboardInterrupt:
    print(term.normal+"bye!")
