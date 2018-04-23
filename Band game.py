import tkinter as tk
import random
    

def Notes():
    print("yo")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="What",
                   fg="cyan",
                   command=Notes)
slogan.pack(side=tk.LEFT)

root.mainloop()


# def how_to_play():
#    print("Type the note in the box that corasponds to the note on the screen.")
