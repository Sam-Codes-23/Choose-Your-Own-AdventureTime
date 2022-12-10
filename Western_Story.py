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

#create photoimage of Western Town
img = Image.open('WesternTown.png')
img_resize = img.resize((500, 400), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img_resize)

#creating a canvas window in the main window to display and set locations of widgets
canvas = tk.Canvas(win, width = 800, height = 500)
canvas.pack()
canvas.create_image((400,250), image=tkimage, tag = "forest")

#create photoimage of Western Saloon
img2 = Image.open('WesternSaloon.png')
img2_resize = img2.resize((500, 400), Image.ANTIALIAS)
tkimage2 = ImageTk.PhotoImage(img2_resize)


#create photoimage of Western Chase
img3 = Image.open('WesternChase.png')
img3_resize = img3.resize((500,400), Image.ANTIALIAS)
tkimage3 = ImageTk.PhotoImage(img3_resize)

#create photoimage of Western Ending
img4 = Image.open('WesternEnding.png')
img4_resize = img4.resize((700,400), Image.ANTIALIAS)
tkimage4 = ImageTk.PhotoImage(img4_resize)

#forest function that will replace campfire image with forest image within the canvas window
def forest():
    canvas.create_image((400,250), image=tkimage2, tag = "hole")
    canvas.itemconfig("forest", image=tkimage2)

#rock wall function that will replace campfire image with rock image within the canvas window
def rock_wall():
    canvas.create_image((400,250), image=tkimage3, tag = "spaceship")
    canvas.itemconfig("hole", image=tkimage3)

#dragon function that will replace rock wall image with dragon image within the canvas window
def dragon():
    canvas.create_image((400,250), image=tkimage4, tag = "ending")
    canvas.itemconfig("spaceship", image=tkimage4)

#creating the text widget to display story - wrap set to word will eliminate word cutoffs
T = Text(win, height = 12, width = 100, wrap=WORD,)
T.place(x=0, y=0) #this places the text widget in the window

Western_1_Story = "\"Welcome to the West!\" cried Harry, as he comes to lead your horse into town. You'll be staying at the Ol' corral there. Would you like to pay a little extra to stable your horse? It'll give her a nice roof and some quality hay. Pay to stable your horse?"
Western_2_Story = "You slide into a booth at the local restaurant and order some food. A sleek man with a large moustache and monacle, all dressed in black wants to speak with you. He asks if you would like to be rich beyond your wildest dreams. All you need to do is give him all the money you have and he will give you the keys to a gold mine. Do you give the man all your money?"
Western_3_Story = "You awake in the night to the sound of shouting from the window. You throw open the shutters to see someone being thrown on the back of a horse by a masked bandit. You could maybe save them if you act fast! Then again, it could put you in a lot of danger. Do you chase them?"
Western_Good = "Horses, gold, and bandits - some days in the West are full of difficult choices! But you made it through either way. It looks like you were a good citizen today."
Western_Bad = "Horses, gold, and bandits - some days in the West are full of difficult choices! But you made it through either way. It looks like you were a bad citizen today."
Western_Choice = 0

def Option_1 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = Western_2_Story
    global Fantasy_Choice #this specifies that the function is changing the global variable and not creating a local variable
    Fantasy_Choice = 1
    b1.after(1, b1.destroy) #destroys button
    b2.after(1, b2.destroy)
    global b3  #creates a global variable to be accessed in other functions
    b3 = Button(win, text = "Yes", command=Option_3)
    global b4 
    b4 = Button(win, text = "No", command = Option_3)
    b3.pack() #adds button to the screen
    b4.pack()
    T.insert(tk.END, Next_Line) #inserts the next line to the Text widget
    T.config(state='disabled')

def Option_2 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = Western_2_Story
    global SciFi_Choice 
    Fantasy_Choice = 2
    b1.after(1, b1.destroy)
    b2.after(1, b2.destroy)
    global b3 
    b3 = Button(win, text = "Yes", command=Option_3)
    global b4 
    b4 = Button(win, text = "No", command = Option_3)
    b3.pack()
    b4.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_3 ():
    T.config(state='normal')
    rock_wall()
    T.delete("1.0", END)
    Next_Line = Western_3_Story
    b3.after(1, b3.destroy)
    b4.after(1, b4.destroy)
    global b5
    global b6
    b5 = Button(win, text = "Yes", command=Option_4)
    b6 = Button(win, text = "No", command=Option_4)
    b5.pack()
    b6.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_4():
    T.config(state='normal')
    dragon()
    T.delete("1.0", END)
    if Fantasy_Choice == 1:
        Next_Line = Western_Good
    if Fantasy_Choice == 2:
        Next_Line = Western_Bad
    b5.after(1, b5.destroy)
    b6.after(1, b6.destroy)
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')



b1 = Button(win, text = "Yes", command=Option_1)
b2 = Button(win, text = "No", command=Option_2)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, Western_1_Story)
T.config(state='disabled') #sets text widget to read only


#keeps window displaying
win.mainloop()
