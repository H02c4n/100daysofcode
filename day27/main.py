from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # expand="True" or side="left"

my_label["text"] = "new Text"
my_label.config(text="New Text")
my_label.place(x=0, y=0)


# Button

def button_clicked():
    print("I got clicked")
    input_text = input.get()
    my_label.config(text=input_text)


button = Button(text="Calculate", command=button_clicked)
button.pack()


#Entry
input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
