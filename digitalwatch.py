from tkinter import *
from time import strftime
# strftime means in giving time according to our computer.
def gettime():
    value = strftime('%H:%M:%S %p')
    timelabel.config(text=value)
    timelabel.after(1000, gettime)
    #after every 1000 miliseconds, update (for seconds)
screen=Tk()
screen.geometry("600x600")
screen.config(background="lightblue")
timelabel = Label(screen, text="", background="ivory", font="Arial, 40")
timelabel.pack(anchor="center")
gettime()
screen.mainloop()