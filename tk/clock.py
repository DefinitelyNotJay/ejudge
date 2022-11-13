""" Clock test """
from tkinter import *
import time
def clock():
    print(time.strftime("%H:%M:%S %p"))
    time.sleep(1)
    clock()
clock()
