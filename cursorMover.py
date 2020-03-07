
import time as t
import random as rand
from pynput.mouse import Controller as mouseController
from pynput.keyboard import Key, Controller
import numpy

#This function will move the cursor every couple of seconds

def cursor_mover():
    start = t.time()
    mouse = mouseController()
    keyboard = Controller()

    while True:
        movedirOne = rand.randint(-100, 100)
        movedirTwo = rand.randint(-100, 100)
        mouse.move(movedirOne, movedirTwo)
        t.sleep(7.0 - ((t.time() - start) % 7))
        keyboard.press(Key.space)

cursor_mover()