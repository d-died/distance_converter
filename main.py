from tkinter import *

window = Tk()
window.title("Convert miles and km")
window.minsize(width=250, height=125)
window.config(padx=20, pady=20)

input_one = Entry(width=10)
input_one.grid(column=1, row=0)

text_one = Label(text="miles")
text_one.grid(column=2, row=0)

equal_to_text = Label(text="is equal to")
equal_to_text.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

text_two = Label(text="KM")
text_two.grid(column=2, row=1)

def calculate():
    num_input = float(input_one.get())
    if text_one["text"] == "miles":
        conversion = num_input * 1.60934
    elif text_one["text"] == "KM":
        conversion = num_input / 1.60934
    answer.config(text=conversion)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=3)

def m_to_km():
    text_one.config(text="miles")
    text_two.config(text="KM")

mkm_button = Button(text="Convert m to km", command=m_to_km)
mkm_button.grid(column=0, row=4)

def km_to_m():
    text_one.config(text="KM")
    text_two.config(text="miles")

kmm_button = Button(text="Convert km to m", command=km_to_m)
kmm_button.grid(column=2, row=4)

window.mainloop()