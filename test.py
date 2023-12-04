# Import Module
from tkinter import *

# create root window
root = Tk()


# root window title and dimension
root.title("Take Home Paycheck Calculator")
# Set geometry(widthxheight)
root.geometry('450x250')

# adding a label to the root window
lbl = Label(root, text="Annual Gross Income: ")
lbl1 = Label(root, text="Federal Income Tax: ")
lbl2 = Label(root, text="Georgia State Income Tax: ")
lbl3 = Label(root, text="Paycheck")

lbl.grid()
lbl1.grid()
lbl2.grid()
lbl3.grid()


# adding Entry Field
#AGI
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

#Federal Income Tax
txt = Entry(root, width=10)
txt.grid(column=1, row=1)

#GA State Tax Income Tax
txt = Entry(root, width=10)
txt.grid(column=1, row=2)

#Paycheck
txt = Entry(root, width=10)
txt.grid(column=1, row=3)

#AGI output
txt = Entry(root, width=10)
txt.grid(column=1, row=5)



# function to display user text when
# button is clicked
def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text=res)


# button widget with red color text inside
btn = Button(root, text="Submit",
             fg="red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=3)




#label for results
results_lbl = Label(root, text="Results ")
#entry for results
results_lbl.grid()


# Execute Tkinter
root.mainloop()