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


#Text
text = Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin
text.insert(END, "Example of multi-line text entry")
#Gets current value in textbox at line 1 , character 0
print(text.get("1.0", END))
text.pack()

#Spinbox

def spinbox_used():
    #gets the curent value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, command=spinbox_used)
spinbox.pack()


#Scale 
#called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton

def checkbutton_used():
    #Print 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, o is off,  is on
checked_state = IntVar()
checked_button = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checked_button.pack()




