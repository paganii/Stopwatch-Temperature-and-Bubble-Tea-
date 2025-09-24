from tkinter import *

screen=Tk()
screen.geometry("550x500")
screen.title("Temperaturr")
screen.config(background="pink")
start_celcius = Label(screen, text="Celcius").place(x=60, y=100)
start_fahrenheit = Label(screen, text="Fahrenheit").place(x=60, y=180)
start_entry_c = Entry(screen, text="Enter celcius")
start_entry_c.place(x=110, y=100)
start_entry_f = Entry(screen, text="Enter Fahrenheit")
start_entry_f.place(x=110, y=180)
def ctof():
    c=start_entry_c.get()
    if c:
        c=float(c) 
        temp = (c*9/5)+32
        Label(screen, text=str(temp)+'F').place(x=110, y=100)
        
def ftoc():
    f=start_entry_f.get()
    if f:
        f=float(f)
        temp = (f-32)/1.8
        Label(screen, text=str(temp)+'C').place(x=110, y=180)
        
c_to_f = Button(screen, text="Convert C to F.", font="Arial, 10", command=ctof).place(x=90, y=210)
f_to_c = Button(screen, text="Convert F to C.", font="Arial, 10", command=ftoc).place(x=400, y=210)
screen.mainloop()