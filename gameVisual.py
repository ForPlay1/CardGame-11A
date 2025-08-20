from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class Button:
    def click(self):
        pass

    def __init__(self, number, image):
        self.number = number
        self.but = ttk.Button(command=self.click, image=image, padding=-4)

    def change_photo(self, image):
        self.but["image"] = image

root = Tk()
root.title("11А")
root.geometry("1920x1080")
root["bg"] = "gray0"

buts = []
images = [ImageTk.PhotoImage(file=f"images/01.{i}.png") for i in range(1,4)]
images.extend([ImageTk.PhotoImage(file=f"images/0{i}.png") for i in range(2, 8)])

for i in range(7):
    button = Button(i, images[i])
    buts.append(button)

for i in range(len(buts)):
    buts[i].but.grid(row=0, column=i, padx=15)


root.mainloop()