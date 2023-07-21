import random



def drawCard():
    card = random.randint(1,10)
    playerHand.append(card)
    return card

def playerTurn():
    input('Press ENTER to draw your first card! ')
    card1 = drawCard()
    input('Press ENTER to draw your second card! ')
    card2 = drawCard()
    print(f"Your cards are {card1} and {card2}.")
    while True:
        response = input("Do you want to HIT or PASS? (1. Hit 2. Pass) ")
        try:
            response = int(response)
            if response == 1:
                card3 = drawCard()
                print(f"You drew a {card3}.")
                cardCount = 0
                for card in playerHand:
                    cardCount += card
                if  cardCount > 21:
                    print("You busted! ")
                    input("Press ENTER to play again! ")
                    return False
                else:
                    print(f"Your cards are {playerHand}")
            elif response == 2:
                cardCount = 0
                for card in playerHand:
                    cardCount += card
                return cardCount
            else:
                print("You need to put either 1. for Hit or 2. for Pass! Try again")
        except:
            print("You need to put either 1. for Hit or 2. for Pass! Try again")

def dealerTurn():
    print("Dealer GOES!")

if __name__=="__main__":
    input("Press ENTER to play! ")
    while True:
        print('''############################
###      Black Jacks     ###
##### By RangerRhino23 #####
############################
        ''')
        playerHand = []
        if playerTurn():
            dealerTurn()

        else:
            print("You Won!")