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

SciFi_1_Story = "You have just landed on an alien planet, your mission is to find a lost diplomat for the Galactic Federation.  Their ship has crash landed somewhere near you and it is pinging on your scanner.  Through a dense alien forest you walk, and come upon a clearing.  In the clearing you see a small rabbit-like creature with very large ears and a big nose.  It seems injured."
SciFi_2_Story = "You forge ahead through the forest and your scanner starts to beep louder.  You must be getting close to the crashed Diplomat ship.  In your way you find a large gap in the ground.  You think maybe you can jump it."
SciFi_3_Story = "Your heart is pounding as you get to the other side and you feel light headed, but just as you are about to pass out your scanner starts to beep wildly.  The ship is so close!  You look around and see it 100 yards away."
SciFi_Good = "You arrive at the ship only to find it empty.  You lose hope and fear the worst.  Just as you are about to turn back and report the diplomat missing, you feel a rubbing at your leg.  It is the alien creature that you helped!  He sniffs around the ship and leads you to a cave a short walk away.  The diplomat is inside and alive! You help him back to his ship, make some repairs, and fly back to the galactic federation.  Mission accomplished and well done."
SciFi_Bad = "You arrive at the ship only the find it empty.  You do not know what to do!  You look around and see no tracks leading away from the ship.  It is like the diplomat vanished into thin air.  Defeated, you fix the crashed ship and fly back to the galactic federation.  Mission failed."
SciFi_Choice = 0

def Option_1 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = SciFi_2_Story
    global Fantasy_Choice #this specifies that the function is changing the global variable and not creating a local variable
    Fantasy_Choice = 1
    b1.after(1, b1.destroy) #destroys button
    b2.after(1, b2.destroy)
    global b3  #creates a global variable to be accessed in other functions
    b3 = Button(win, text = "Try and jump the gap to save valuable time.", command=Option_3)
    global b4 
    b4 = Button(win, text = "Walk around the gaping chasm and eventually get to the other side", command = Option_3)
    b3.pack() #adds button to the screen
    b4.pack()
    T.insert(tk.END, Next_Line) #inserts the next line to the Text widget
    T.config(state='disabled')
   

def Option_2 ():
    T.config(state='normal')
    forest()
    T.delete("1.0", END)
    Next_Line = SciFi_2_Story
    global SciFi_Choice 
    Fantasy_Choice = 2
    b1.after(1, b1.destroy)
    b2.after(1, b2.destroy)
    global b3 
    b3 = Button(win, text = "Try and jump the gap to save valuable time.", command=Option_3)
    global b4 
    b4 = Button(win, text = "Walk around the gaping chasm and eventually get to the other side", command = Option_3)
    b3.pack()
    b4.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_3 ():
    T.config(state='normal')
    rock_wall()
    T.delete("1.0", END)
    Next_Line = SciFi_3_Story
    b3.after(1, b3.destroy)
    b4.after(1, b4.destroy)
    global b5
    global b6
    b5 = Button(win, text = "Rush towards the ship and see if the diplomat is inside.", command=Option_4)
    b6 = Button(win, text = "Take your time since you are very weary from your traveling.", command=Option_4)
    b5.pack()
    b6.pack()
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')

def Option_4():
    T.config(state='normal')
    dragon()
    T.delete("1.0", END)
    if Fantasy_Choice == 1:
        Next_Line = SciFi_Good
    if Fantasy_Choice == 2:
        Next_Line = SciFi_Bad
    b5.after(1, b5.destroy)
    b6.after(1, b6.destroy)
    T.insert(tk.END, Next_Line)
    T.config(state='disabled')



b1 = Button(win, text = "Stop to help the potentially dangerous creature before continuing on your way", command=Option_1)
b2 = Button(win, text = "Continue on your way without stopping", command=Option_2)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, SciFi_1_Story)
T.config(state='disabled') #sets text widget to read only


#keeps window displaying
win.mainloop()
