from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=150, pady=50)

#Convert function

def miles_to_km():
    miles = float(input.get())
    km = round(miles*1.609)
    result.config(text=f"{km}")
    

#LABEL
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

#INPUT
input = Entry(width=7)
input.grid(column=1, row=0)
mile = input.get()


#RESULT
result = Label(text="0")
result.grid(column=1, row=1)


#BUTTON
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()