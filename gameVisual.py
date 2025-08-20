from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class Button:
    def click(self):
        self.change_photo(images[self.number + 1])

    def __init__(self, number, image):
        self.number = number
        self.but = ttk.Button(command=self.click, image=image)

    def change_photo(self, image):
        self.but["image"] = image

root = Tk()
root.title("11А")
root.geometry("1920x1080")

buts = []
images = [ImageTk.PhotoImage(file=f"images/01.{i}.png") for i in range(1,4)]
images.extend([ImageTk.PhotoImage(file=f"images/0{i}.png") for i in range(2, 8)])

for i in range(7):
    button = Button(i, images[i])
    buts.append(button)

for i in range(len(buts)):
    buts[i].but.grid(row=0, column=i, padx=15)




root.mainloop()