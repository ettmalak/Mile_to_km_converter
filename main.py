from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=350)
window.config(pady=30, padx=30)

mile_value = IntVar()
mile_value.set(0)
mile_nr = Entry(textvariable=mile_value)
mile_nr.grid(column=1, row=0)

km_value = StringVar(value="0")

def convert_miles():
    user_input = int(mile_nr.get())
    kms = round(user_input*1.609344)
    km_value.set(str(kms))

mile = Label(text="Miles")
mile.grid(column=2, row=0)

my_Label = Label(text="is equalt to ")
my_Label.grid(column=0, row=1)

Km_nr = Label(textvariable=km_value)
Km_nr.grid(column=1, row=1)

Km = Label(text="Km")
Km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_miles)
button.grid(column=1, row=2)






window.mainloop()