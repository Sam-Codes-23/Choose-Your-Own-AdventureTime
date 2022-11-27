# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *



#create window
win = Tk()



#size of window
win.geometry("1200x800")

#window title
l = Label(win, text = "Choose Your Own AdventureTime")
l.config(font = ("Courier", 14))

#Fantasy Story Slides
T = Text(win, height = 12, width = 100)

Fantasy_1_Story = "You are an adventurer and have taken up the job of searching for the reason why the land has plunged into darkness and the missing King. You are walking along a road through the forest and come across an old man by a fire. He looks sick and hungry, but also mysterious. You are tempted to help, but then you realize that you do not know him. Should you help him? "
Fantasy_2_Story = "You leave the old man behind and continue your journey. There is a fork in the forest path and you have to choose which way you should go. The path to the left seems dark and haunted. The path to the right has spots of sunshine from the treetops. Which path do you decide to take?"
Fantasy_3_Story = "The path you choose ends up being a dead end, with an abandoned cabin. You search the cabin, but don�t find anything that can help you on your quest. You loop back and go down the different path. You come across the castle that the dragon has taken over. You must decide to risk going in the entrance or sneaking your way in from the side."
Fantasy_Good = "The old man you saved suddenly appears besides you and reveals he is a powerful wizard. The wizard says the entrance is barred, but he can teleport you inside. He also give you a magical protection stone to help you against the darkness. Once inside the dragon starts to attack, but senses the magical protection stone the wizard gave you. As the dragon is distracted, the wizard casts a powerful spell, which turns the dragon back into the missing King! The King thanks you and returns to the Castle and a big celebration feast is enjoyed by the entire Kingdom!"
Fantasy_Bad = "You enter the castle and find the dragon waiting in the courtyard. You are able to banish the dragon, which lifts the darkness from the realm, but you are unable to find the missing King anywhere. You return to the castle and live out your days as a simple blacksmith as there are no adventures without the King."
Fantasy_Choice = TRUE

def Option_1 ():
    T.delete("1.0", END)
    Next_Line = Fantasy_2_Story
    b1 = Button(win, text = "You decide to plunge deeper into the darkness and take the path to the left.", command=Option_3)
    T.insert(tk.END, Next_Line)

def Option_2 ():
    T.delete("1.0", END)
    Next_Line = Fantasy_2_Story
    T.insert(tk.END, Next_Line)

def Option_3 ():
    T.delete("1.0", END)
    Next_Line = Fantasy_3_Story



b1 = Button(win, text = "You help him by giving him some water and Elvish bread.", command=Option_1)
b2 = Button(win, text = "You do not help him, but you keep walking.", command=Option_2)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END, Fantasy_1_Story)


#keeps window displaying
win.mainloop()