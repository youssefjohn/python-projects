from tkinter import *

def button_clicked():
    new_label = input.get()
    label.config(text=new_label)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
label['text'] = "New label"
label.config(text="New label")

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=2,row=0)



# Entry


input = Entry(width=10)
input.grid(column=3, row=2)




window.mainloop()
