from random import shuffle

def printCards():
    print("Номера удерживаемых карт: ", ", ".join(map(str, [c.number for c in players[tecPlayer].cardDeck])))

def choosePlayerForAttack():
    if len([1 for player in players if player.block == 0]) > 0:
        print("Игроки: ", ", ".join([f"Игрок #{players[i].number} - {players[i].name}" for i in range(len(players))]))
        return choosesmth("Выберите номер игрока для атаки по порядку: ", 1, len(players), *[num+1 for num in range(len(players)) if players[num].block != 0]) - 1
    print("Все игроки под защитой")
    return -1

def choosesmth(mes, minim, maxim, *forb):
    chosn = int(input(mes))
    while chosn < minim or chosn > maxim or chosn in forb:
        forby = "Запрещаются числа: " + ", ".join(map(str, forb)) + ". " if forb else ""
        chosn = int(input(f"Неправильный выбор. Введите номер от {minim} до {maxim}. " + forby + "Ваше число: "))
    return chosn
    
    
class Card():
    def __init__(self, number: int):
        self.number = number

        
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
        pdeck.append(Card(8))
    pdeck.append(Card(0))
    pdeck.append(Card(-1))
    pdeck.append(Card(9))
    shuffle(pdeck)
    return pdeck


def useCard(deck, usedDeck, players, tecPlayer, tecCard):
    match players[tecPlayer].cardDeck[tecCard].number:
        case 1:
            chosenAttackPlayer = choosePlayerForAttack()
            if chosenAttackPlayer == -1:
                return
            chosenAttackCard = choosesmth("Выберите номер карты, которую вы хотите выбить: ", 1, 40, 9)
            if chosenAttackCard in[ car.number for car in players[chosenAttackPlayer].cardDeck]:
                print("Попал")
                players[chosenAttackPlayer].removeCard(chosenAttackCard, 1)
            else:
                print("Не попал")
        case 2:
            chosenAttackPlayer = choosePlayerForAttack()
            if chosenAttackPlayer == -1:
                return
            shufdeck = [car.number for car in players[chosenAttackPlayer].cardDeck]
            shuffle(shufdeck)
            if len(shufdeck)>3:
                chosenAttackCards = []
                for _ in range(3):
                    chosenAttackCards.append(choosesmth(f"Выберите одну из его карт по сче́ту для просмотра(1-{len(shufdeck)}): ", 1, len(shufdeck), *chosenAttackCards))
                print(", ".join(map(str, [shufdeck[i-1] for i in chosenAttackCards])))
            else:
                print(", ".join(map(str, shufdeck)))
        case 3:
            players[tecPlayer].block += 1
        case 4:
            chosenAttackPlayer = choosePlayerForAttack()
            if chosenAttackPlayer == -1:
                return
            chosenAttackCard = choosesmth("Выберите номер карты, которую вы хотите выбить: ", 1, 40, 9)
            if chosenAttackCard in[ car.number for car in players[chosenAttackPlayer].cardDeck]:
                print("Попал")
                players[chosenAttackPlayer].removeCard(chosenAttackCard, 1)
            else:
                print("Не попал")
            chosenAttackCard = choosesmth("Выберите номер карты, которую вы хотите выбить: ", 1, 40, 9)
            if chosenAttackCard in[ car.number for car in players[chosenAttackPlayer].cardDeck]:
                print("Попал")
                players[chosenAttackPlayer].removeCard(chosenAttackCard, 1)
            else:
                print("Не попал")
        case 5:
            chosenAttackPlayer = choosePlayerForAttack()
            if chosenAttackPlayer == -1:
                return
            shufdeck = [car.number for car in players[chosenAttackPlayer].cardDeck]
            shuffle(shufdeck)
            chosenAttackCard = choosesmth(f"Выберите номер карты, которую вы хотите выбить из его по порядку(1-{len(shufdeck)}): ", 1, len(shufdeck))-1
            players[chosenAttackPlayer].removeCard(shufdeck[chosenAttackCard], 5)
            print(f"Выбитая карта: {shufdeck[chosenAttackCard]}")
        case 6:
            players[tecPlayer].maxCards += 0.5 + (players[tecPlayer].maxCards % 1)
        case 8:
            chosenAttackPlayer = choosePlayerForAttack()
            if chosenAttackPlayer == -1:
                return
            players[chosenAttackPlayer].skipTurns += 1
    
    
deck = createDeck()
usedDeck = []
playerCount = int(input("Введите количество игроков: "))
if playerCount*7>len(deck):
    print(f"Слшком много игроков, максимум: {len(deck)//7}")
    exit()
players = []
for i in range(1, playerCount+1):
    players.append(Player(input(f"Введите имя игрока #{i}: "), i))
tecPlayer = 0 # кто ближе к егору
for _ in range(7):
    for i in range(playerCount):
        players[i].cardDeck.append(deck.pop(0))
while len([1 for player in players if player.live]) > 1:
    if -1 in [card.number for card in players[tecPlayer].cardDeck]:
        players[tecPlayer].maxCards = 8
    print(f"Игрок #{tecPlayer+1} {players[tecPlayer].name}")
    if players[tecPlayer].block > 0:
        players[tecPlayer].block -= 1
    if players[tecPlayer].skipTurns > 0:
        players[tecPlayer].skipTurns -= 1
        print("Пропуск хода")
    else:
        printCards()
        tecCard = choosesmth("Номер используемой карты по порядку: ", 1, len(players[tecPlayer].cardDeck)) - 1
        useCard(deck, usedDeck, players, tecPlayer, tecCard)
        players[tecPlayer].cardDeck.pop(tecCard)
    while len(deck)>0 and len(players[tecPlayer].cardDeck) < players[tecPlayer].maxCards:
        players[tecPlayer].cardDeck.append(deck.pop(0))
        for i in range(len(players)):
            while len(deck)>0 and len(players[i].cardDeck) < players[i].maxCards:
                players[i].cardDeck.append(deck.pop(0))
    players[tecPlayer].maxCards = 7
    printCards()
    tecPlayer += 1
    if tecPlayer == playerCount:
        tecPlayer = 0
    input("Переход к следующему игроку(Enter для перехода)...")