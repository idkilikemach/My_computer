# TODO digital_watch is unfinished
from os import times
from tkinter import *
import datetime
time = datetime.datetime.now()
print(time.strftime("%H, %M, %S"))

time_watch = Tk()
time_watch.geometry("400x300")

time_watch.mainloop()