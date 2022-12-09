## -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk



#create window
win = Tk()




#size of window

app_width = 1280
app_height = 1024
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
win.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
win.configure(background='light blue')


#window title
l = Label(win, text = "Choose Your Own AdventureTime")
l.config(font = ("Courier", 14))

#create photoimage of campfire
img = Image.open('camp_fire1.jpg')
img_resize = img.resize((500, 400), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img_resize)

#creating a canvas window in the main window to display and set locations of widgets
canvas = tk.Canvas(win, width = 800, height = 500)
canvas.pack()
canvas.create_image((400,250), image=tkimage, tag = "campfire")

#create photoimage of forest
img2 = Image.open('Forest.jpg')
img2_resize = img2.resize((500, 400), Image.ANTIALIAS)
tkimage2 = ImageTk.PhotoImage(img2_resize)


#create photoimage of rock wall
img3 = Image.open('rock_wall.jpg')
img3_resize = img3.resize((500,400), Image.ANTIALIAS)
tkimage3 = ImageTk.PhotoImage(img3_resize)

#create photoimage of dragon defeated
img4 = Image.open('dragon.jpg')
img4_resize = img4.resize((700,400), Image.ANTIALIAS)
tkimage4 = ImageTk.PhotoImage(img4_resize)

#forest function that will replace campfire image with forest image within the canvas window
def forest():
    canvas.create_image((400,250), image=tkimage2, tag = "forest")
    canvas.itemconfig("campfire", image=tkimage2)


#rock wall function that will replace campfire image with rock image within the canvas window
def rock_wall():
    canvas.create_image((400,250), image=tkimage3, tag = "rock")
    canvas.itemconfig("forest", image=tkimage3)

#dragon function that will replace rock wall image with dragon image within the canvas window
def dragon():
    canvas.create_image((400,250), image=tkimage4, tag = "dragon")
    canvas.itemconfig("rock", image=tkimage4)

#creating the text widget to display story - wrap set to word will eliminate word cutoffs
T = Text(win, height = 12, width = 100, wrap=WORD,)
T.place(x=0, y=0) #this places the text widget in the window

Fantasy_1_Story = "You are an adventurer and have taken up the job of searching for the reason why the land has plunged into darkness and to find the missing King. You are walking along a road through the forest and come across an old man by a fire. He looks sick and hungry, but also mysterious. You are tempted to help, but then you realize that you do not know him. Should you help him? "
Fantasy_2_Story = "You leave the old man behind and continue your journey. There is a fork in the forest path and you have to choose which way you should go. The path to the left seems dark and haunted. The path to the right has spots of sunshine from the treetops. Which path do you decide to take?"
Fantasy_3_Story = "The path is a dead end at an abandoned cabin. You happen to spot an opening in the rock wall behind the cabin and you squeeze through it. This path takes you to the castle with the dragon. Should you risk going in the entrance or sneak your way in from the side?"
Fantasy_Good = "The old man you saved suddenly appears besides you and reveals he is a powerful wizard. The wizard says the entrance is barred, but he can teleport you inside. He also give you a magical protection stone to help you against the darkness. Once inside the dragon starts to attack, but senses the magical protection stone the wizard gave you. As the dragon is distracted, the wizard casts a powerful spell, which turns the dragon back into the missing King! The King thanks you and returns to the Castle and a big celebration feast is enjoyed by the entire Kingdom!"
Fantasy_Bad = "You enter the castle and find the dragon waiting in the courtyard. You are able to banish the dragon, which lifts the darkness from the realm, but you are unable to find the missing King anywhere. You return to the castle and live out your days as a simple blacksmith as there are no adventures without the King."
Fantasy_Choice = 0

def Option_1 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = Fantasy_2_Story
    global Fantasy_Choice #this specifies that the function is changing the global variable and not creating a local variable
    Fantasy_Choice = 1
    b1.after(1, b1.destroy) #destroys button
    b2.after(1, b2.destroy)
    global b3  #creates a global variable to be accessed in other functions
    b3 = Button(win, text = "You decide to plunge deeper into the darkness and take the path to the left.", command=Option_3)
    global b4 
    b4 = Button(win, text = "The sunshine is too tempting to pass up, so you decide to go right.", command = Option_3)
    b3.pack() #adds button to the screen
    b4.pack()
    T.insert(tk.END, Next_Line) #inserts the next line to the Text widget
    T.config(state='disabled')
   

def Option_2 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = Fantasy_2_Story
    global Fantasy_Choice 
    Fantasy_Choice = 2
    b1.after(1, b1.destroy)
    b2.after(1, b2.destroy)
    global b3 
    b3 = Button(win, text = "You decide to plunge deeper into the darkness and take the path to the left.", command=Option_3)
    global b4 
    b4 = Button(win, text = "The sunshine is too tempting to pass up, so you decide to go right.", command = Option_3)
    b3.pack()
    b4.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_3 ():
    T.config(state='normal')
    rock_wall()
    T.delete("1.0", END)
    Next_Line = Fantasy_3_Story
    b3.after(1, b3.destroy)
    b4.after(1, b4.destroy)
    global b5
    global b6
    b5 = Button(win, text = "You are brave and decide to run through the main entrance and fight the dragon head on!", command=Option_4)
    b6 = Button(win, text = "You want to get more information before taking on the dragon, so you decide it's best to sneak in the side of the castle.", command=Option_4)
    b5.pack()
    b6.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_4():
    T.config(state='normal')
    dragon()
    T.delete("1.0", END)
    if Fantasy_Choice == 1:
        Next_Line = Fantasy_Good
    if Fantasy_Choice == 2:
        Next_Line = Fantasy_Bad
    b5.after(1, b5.destroy)
    b6.after(1, b6.destroy)
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')



b1 = Button(win, text = "You help him by giving him some water and Elvish bread.", command=Option_1)
b2 = Button(win, text = "You do not help him, but you keep walking.", command=Option_2)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, Fantasy_1_Story)
T.config(state='disabled') #sets text widget to read only


#keeps window displaying
win.mainloop()
