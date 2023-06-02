from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")


#calls action when pressed

button = Button(text="Click me", command=action)
button.pack()

#Entris

entry = Entry(width=30)
#add some text to begin with
entry.insert(END, string="Some text to begin with")
#gets text in entry
print(entry.get())
entry.pack()


