from tkinter import *
GREEN = "#9bdeac"

OPTIONS = [
"401k",
"Roth IRA",
"HSA"
] #etc

OPTIONS_PAYMENT_SCHEDULE = [
    "Bi-Weekly"
    "Semi-Monthly"
]

# Calculates the semi-monthly income
def submit_clicked():
    print("Submit button was clicked")
    #my_label.config(text="Submit button was clicked")


window = Tk()
window.title("Take Home Pay Calculator GUI")
window.config(padx=10,pady=20,bg=GREEN)

canvas = Canvas(width=700, height=600, highlightthickness=0,bg=GREEN)
payday_image = PhotoImage(file="payday_image.png")
canvas.create_image(350,300,image=payday_image)
canvas.grid(column=0,row=0,columnspan=2)

#Labels
gross_income_label = Label(text="Annual Gross Income: ")
gross_income_label.grid(column=0,row=2)
state_label = Label(text="State of Residence:")
state_label.grid(column=0,row=4)


#Entry
gross_income_entry = Entry(width=10)
gross_income_entry.grid(column=1, row=2)
state_label = Entry(width=10)
state_label.grid(column=1,row=4)

#submit button
submit_button = Button(text="Submit", command=submit_clicked)
submit_button.grid(column=1,row=6)
#clear button
clear_button = Button(text="Clear")
clear_button.grid(column=0,row=6)

#Entry is our input command
# input = Entry(width=20)
# input.insert(END, string="Annual Salary.. ")
# input.grid(column=0,row=3)

# get() method of input will get the value of what the user entered
# input.get()


#RadioButton

def radio_used():
    print(radio_state.get())

#variable to hold onto which radio button is checked

radio_state = IntVar()
semimonthlyradiobutton = Radiobutton(text="Semi-Monthly", value=1, variable=radio_state, command=radio_used)
twice_a_month = Radiobutton(text="Twice-a-Month", value=2, variable=radio_state, command=radio_used)
semimonthlyradiobutton.grid(column=0,row=3)
twice_a_month.grid(column=0,row=4)



#keeps the window on the screen
#should always be at the very end of the program
window.mainloop()