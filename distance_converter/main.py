from tkinter import *

def miles_to_km():
    miles = float((entry.get()))
    km = round(miles * 1.6)
    calculation_label.config(text=(f"{km}"))


window = Tk()
window.minsize(width=150, height=50)
window.config(padx=100, pady=100)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=0)
miles_label.config()

is_equal_to_label = Label(text="is equal to", font=("Arial", 12))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config()

km_label = Label(text="km", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config()

calculation_label = Label(text=0, font=("Arial", 12))
calculation_label.grid(column=1, row=1)


entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()













