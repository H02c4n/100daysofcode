from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # expand="True" or side="left"

my_label["text"] = "new Text"
my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text="Last version")


button = Button(text="Calculate", command=button_clicked)
button.pack()

window.mainloop()
