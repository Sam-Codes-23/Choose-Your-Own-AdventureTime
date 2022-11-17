from gc import callbacks
import tkinter as tk
from tkinter import ttk


#create window
root = tk.Tk()

#size of window
root.geometry('600x400+50+50')
window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#window title
root.title('Choose Your Own AdventureTime')

#place a message
message = tk.Label(root, text = "Hello World!")
message.pack()

#create an exit button
exit_button = ttk.Button(
    root,
    text = 'Exit',
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
   )


#keeps window displaying
root.mainloop()