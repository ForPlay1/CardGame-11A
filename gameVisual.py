from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from random import randint, shuffle


class Player():
    def __init__(self, name, number):
        self.name = name
        self.cardDeck = []
        self.number = number
        self.live = True
        self.block = 0
        self.maxCards = 7
        self.skipTurns = 0
        
    def removeCard(self, attacked, bywhat):
        self.cardDeck.pop([self.cardDeck.index(cary) for cary in self.cardDeck if cary.number == attacked][0])


class Card:
    def click(self):
        self.but.grid_forget()
        print(self.number)

    def __init__(self, number):
        self.number = number
        if number == 1:
            self.but = ttk.Button(command=self.click, image=images[randint(0, 2)], padding=-4)
        else:
            self.but = ttk.Button(command=self.click, image=images[number+1], padding=-4)

    def change_photo(self, image):
        self.but["image"] = image


def createDeck():
    pdeck = []
    for i in range(7):
        pdeck.append(Card(1))
        pdeck.append(Card(2))
        pdeck.append(Card(3))
    for i in range(5):
        pdeck.append(Card(4))
        pdeck.append(Card(5))
        pdeck.append(Card(6))
        pdeck.append(Card(7))
    #     pdeck.append(Card(8))
    # pdeck.append(Card(41))
    # pdeck.append(Card(42))
    # pdeck.append(Card(43))
    shuffle(pdeck)
    return pdeck


def check(namePlayer: str) -> int:
    ult = "егор"
    alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    res = 0
    for i in range(min(4, len(namePlayer))):
        res += abs(alp.index(namePlayer[i])-alp.index(ult[i]))
    return res
    

def checkInPlayer():
    global playerCount, tecplayer, players, textTurn
    players.append(Player(typein.get(), tecplayer))
    if len(players) < playerCount:
        tecplayer += 1
        textPlayers['text'] = f'Имя игрока #{tecplayer}'
        typein.delete(0, len(typein.get()))
        return
    scores = [check(player.name.lower()) for player in players]
    minScore = min(scores)
    if scores.count(minScore) == 1:
        tecplayer = scores.index(minScore)
    else:
        randList = [i for i in range(len(scores)) if scores[i] == minScore]
        tecplayer = randList[randint(len(randList))]
    for _ in range(7):
        for i in range(playerCount):
            players[i].cardDeck.append(cardDeck.pop(0))
    textPlayers.pack_forget()
    butReady.pack_forget()
    typein.pack_forget()
    textTurn['text'] = f'Игрок №{tecplayer+1}: {players[tecplayer].name}'
    textTurn.grid(row=0, padx=10, pady=10)
    for i in range(len(players[tecplayer].cardDeck)):
        players[tecplayer].cardDeck[i].but.grid(row=1, column=i, padx=15, pady=10)


def startGame():
    global playerCount, tecplayer
    if not typein.get().isdigit():
        aware['text'] = 'Not a number!'
        return
    playerCount = int(typein.get())
    if playerCount < 2 or playerCount > 21:
        aware['text'] = 'You picked wrong number, it should be between 2 and 21'
        return
    aware.pack_forget()
    textPlayers['text'] = f'Имя игрока #{tecplayer}'
    butReady['command'] = checkInPlayer
    typein.delete(0, len(typein.get()))

# Root
root = Tk()
root.title("11А")
root.geometry("1920x1080")
root["bg"] = "gray0"

# Textures
images = [ImageTk.PhotoImage(file=f"images/01.{i}.png") for i in range(1,4)]
images.extend([ImageTk.PhotoImage(file=f"images/0{i}.png") for i in range(2, 8)])

# Useful variables
cardDeck = createDeck()
usedDeck = []
players = []
tecplayer = 1
playerCount = 0

# Widgets in the start
textPlayers = ttk.Label(text="Сколько игроков будет играть?(2-21)")
typein = ttk.Entry()
butReady = ttk.Button(text="Подтвердить", command=startGame)
aware = ttk.Label(foreground="red")
textPlayers.pack(padx=10, pady=10)
typein.pack(padx=10, pady=10)
butReady.pack(padx=10, pady=10)
aware.pack(padx=10, pady=10)

# Widgets in the game
textTurn = ttk.Label() # Whos turn

# for i in range(randint(2, len(cardDeck))):
#     cardDeck[i].but.grid(row=0, column=i, padx=15)

root.mainloop()