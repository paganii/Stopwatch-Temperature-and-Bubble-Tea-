from tkinter import *
from tkinter import messagebox
from tkinter import ttk
screen=Tk()
screen.geometry("680x500")
screen.config(background="lightblue")

Label(screen, text="Bubble Tea Shop", font="Arial, 10").place(x=270, y=60)
Label(screen, text="Choose your favorite base", font="Arial, 10").place(x=105, y=120)
basevariable = StringVar()
basechoice=ttk.Combobox(screen, textvariable=basevariable, state="readonly", values=["Black tea", "Green tea", "Oolong tea", "Chamomile tea", "Milk Tea", "Thai tea"])
# state="readonly" is to set that options can only be selected, not changed by writing ourselves.
basechoice.place(x=105, y=143)
basechoice.current(4) # Choose which menu option to display by index number

Label(screen, text="Choose your milk", font="Arial, 10").place(x=305, y=120)
milkvariable = StringVar()
milkchoice=ttk.Combobox(screen, textvariable=milkvariable, state="readonly", values=["Oat milk", "Plant milk", "Soy milk", "Almond milk", "Fresh milk"])
milkchoice.place(x=305, y=143)
milkchoice.current(4)

Label(screen, text="Choose your sweetness level (sugar amount)", font="Arial, 10").place(x=105, y=200)
sugarvar = StringVar()
sugarchoice=ttk.Combobox(screen, textvariable=sugarvar, state="readonly", values=["0%", "25%", "50%", "75%", "100%"])
sugarchoice.place(x=105, y=223)
sugarchoice.current(1)

Label(screen, text="Choose your toppings", font="Arial, 10").place(x=395, y=200)
topvar = StringVar()
topschoice=ttk.Combobox(screen, textvariable=topvar, state="readonly", values=["Oreo", "Grass Jelly", "Sago", "Coconut Jelly", "Red Beans"])
topschoice.place(x=395, y=223)
topschoice.current(1)

def success():
    messagebox.showinfo("Info", "909: Your order is placed. Staff will catch up in 10 minutes.")
    
placeorder = Button(screen, text="Place order", command=success).place(x=310, y = 340)
screen.mainloop()