from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


def calculate_km():
    num = input_box.get()
    calculation = float(num) * 1.609344
    answer.config(text=calculation)


equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

button = Button(text="Click Me", command=calculate_km)
button.grid(column=1, row=2)

answer = Label(text="0")
answer.grid(column=1, row=1)

window.mainloop()
