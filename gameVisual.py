from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class Button:
    def __init__(self, number, image):
        self.number = number
        self.but = ttk.Button(text="Press", command=lambda:print(self.number), image=image)

    def change_photo(self, image):
        self.but["image"] = image

root = Tk()

def click_button():
    print((root.winfo_pointerx() - root.winfo_rootx())//125)

root.title("Тестовый")
root.geometry("1920x1080")
buts = []
image = ImageTk.PhotoImage(file="images/01.png")
image2 = ImageTk.PhotoImage(file="images/02.png")
for i in range(7):
    button = Button(i, image)
    buts.append(button)
buts[1].change_photo(image2)

for i in range(len(buts)):
    buts[i].but.grid(row=0, column=i, padx=15)

root.mainloop()