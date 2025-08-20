from tkinter import *
from tkinter import ttk
from PIL import ImageTk

root = Tk()
clicks = 0

def click_button():
    global clicks
    clicks += 1
    buts[(root.winfo_pointerx() - root.winfo_rootx())//107]["text"] = f"Clicks: {clicks}"

root.title("Тестовый")
root.geometry("1920x1080")
buts = []
image = ImageTk.PhotoImage(file="images/01.png")
for i in range(7):
    but = ttk.Button(text="Press", command=click_button, image=image)
    but.grid(row=0, column=i, padx=15)
    buts.append(but)

root.mainloop()