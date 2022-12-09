from tkinter import *
from PIL import ImageTk, Image
import runpy #module to run other python files


#This creates the main window of an application
root = Tk()
root.title("Choose Your Own AdventureTime!")
app_width = 1280
app_height = 1024
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(background='light blue')
astro_path = "astronaut.jpg"
cBoy_path = "cowboy.jpg"
wizard_path = "wizard.jpg"
mainmenu_path = "mainmenu.jpg"

#Create Button Definitions
def close():
    root.destroy()

#Function to run fantasy story
def runFantasy():
    root.destroy() #must close window in order to run new story
    runpy.run_path(path_name='Fantasy_Story.py')

#Function to run scifi story
def runScifi():
    root.destroy()
    runpy.run_path(path_name = 'SciFi_Story.py')

#Astronaut Image Import
astro_image_pre = Image.open(astro_path)
resize_image = astro_image_pre.resize((150,300))
img = ImageTk.PhotoImage(resize_image)
astro_image_final = Label(image = img)
astro_image_final.place(x = 990, y = 400)

#Cowboy Image Import
cBoy_image_pre = Image.open(cBoy_path)
resize_image2 = cBoy_image_pre.resize((150,300))
img2 = ImageTk.PhotoImage(resize_image2)
cBoy_image_final = Label(image = img2)
cBoy_image_final.place(x = 110, y = 400)

#Wizard Image Import
wizard_image_pre = Image.open(wizard_path)
resize_image3 = wizard_image_pre.resize((150,300))
img3 = ImageTk.PhotoImage(resize_image3)
wizard_image_final = Label(image = img3)
wizard_image_final.place(x = 560, y = 400)

#Title Image Import
mainmenu_image_pre = Image.open(mainmenu_path)
resize_image4 = mainmenu_image_pre.resize((1280,300))
img4 = ImageTk.PhotoImage(resize_image4)
mainmenu_image_final = Label(image = img4)
mainmenu_image_final.place(x = 0, y = 0)

#Character Selection Buttons
cBoy = Button(root, text = "Cowboy",  height=8, width = 50, bg = '#ffca18')
wizard = Button(root, text = "Wizard", height = 8, width = 50, bg = '#d31212', command=runFantasy)
astro = Button(root, text = "Astronaut", height = 8, width = 50, bg = '#ffca18', command = runScifi)
exit_to_dt = Button(root, text = "Quit to Desktop", height = 5, width = 25, bg = '#00a8f3', command = close)

cBoy.place(x = 25, y = 750)
wizard.place(x = 460, y = 750)
astro.place(x = 890, y = 750)
exit_to_dt.pack(side = BOTTOM)


#Start the GUI
root.mainloop()
