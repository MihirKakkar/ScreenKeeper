import time as t
import random as rand
from pynput.mouse import Controller as mouseController
from pynput.keyboard import Key, Controller, Listener
import keyboard as keyb

# This function will move the cursor and press space every couple of seconds

def cursor_mover():
    start = t.time()
    mouse = mouseController()
    keyboard = Controller()

    while True:
        # Random movements
        movedirX = rand.randint(-100, 100)
        movedirY = rand.randint(-100, 100)

        mouse.move(movedirX, movedirY)
        keyboard.press(Key.space)

        # Every _ seconds
        t.sleep(2.0 - ((t.time() - start) % 2))

    #if keyb.:
    #    check = t.time()
    #    runtime = str(check - start)
    #    print("You have been running this for " + runtime + " seconds.")


cursor_mover()
