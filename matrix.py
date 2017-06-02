# builtin packages
from sys import stdout
from time import sleep
import random
import os

#additional packages > install using pip install <NAMEOFPACKAGE>
import noise
from blessings import Terminal

interval = 0.001

term = Terminal()
width = term.width
height = term.height

possible_locations_columns = []
column_spacing = 7

for x in range (0, int(width/column_spacing)):
    possible_locations_columns.append(x*column_spacing)

# get_rid_of_top_line = ""
os.system("clear")

def random_move_drawing():
    while True:
        with term.location(possible_locations_columns[random.randint(0, len(possible_locations_columns)-1)], random.randint(1, height-2)):
            print(term.green+str(random.randint(0, 9)))
            term.location()


try:
    random_move_drawing()
except KeyboardInterrupt:
    print(term.white+"bye!")
