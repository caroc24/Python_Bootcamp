from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input_box.get()
    button.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button_two = Button(text="Click Me", command=button_clicked)
button_two.grid(column=2, row=0)

# Entry
input_box = Entry(width=10)
print(input_box.get())
input_box.grid(column=3, row=2)


window.mainloop()
