from tkinter import *
from tkinter import messagebox
from time import time
screen=Tk()
screen.title("Stopwatch")
screen.geometry("700x570")
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")
screen.config(background="gray")
def submit():
    try:
        temp=int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())
    except:
        print("Please input the right value.")
    while temp>-1:
        minute, second = divmod(temp, 60)
        hour=00
    if minutes>60:
        hour.minute=divmod(minute, 60)
    hour.set("{00:2d}".format(hour))
    minute.set("{00:2d}".format(minute))
    second.set("{00:2d}".format(second))
    screen.update()
    time.sleep(1)
    if temp == 00:
        messagebox.showinfo("Time Countdown", "Time's up!!")
    temp-1 
hours = Entry(screen, w=3, font=20, textvariable=hour)
hours.place(x=80, y=40)
minutes = Entry(screen, w=3, font=20, textvariable=minute)
minutes.place(x=130, y=40)
seconds = Entry(screen, w=3, font=20, textvariable=second)
seconds.place(x=180, y=40)

setcountdown = Button(screen, text="Countdown", bd="5", command=submit).place(x=130, y=100)
screen.mainloop()