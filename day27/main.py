from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)
# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#! my_label.pack()  # expand="True" or side="left"

my_label["text"] = "new Text"
my_label.config(text="New Text")
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("I got clicked")
    input_text = input.get()
    my_label.config(text=input_text)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=1)

new_btn = Button(text="New button")
new_btn.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)

window.mainloop()
