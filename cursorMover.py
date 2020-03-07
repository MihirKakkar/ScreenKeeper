
import time as t
import random as rand
from pynput.mouse import Controller
import numpy

#This function will move the cursor every couple of seconds

def cursor_mover():
    start = t.time()
    mouse = Controller()
    i = 0

    while True:

        movedirOne = rand.randint(1, 100)
        movedirTwo = rand.randint(1, 100)
        mouse.move(movedirOne, movedirTwo)
        t.sleep(2.0 - ((t.time() - start) % 2))
        i += 1

cursor_mover()