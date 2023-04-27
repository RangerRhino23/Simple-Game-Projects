import random


choices = ['rock','paper','scissors']

if __name__ == '__main__':
    while True:
        userChoice = input('1) Rock 2) Paper 3) Scissors, type 1,2,or 3 for you answer: ')
        try:
            userChoice = int(userChoice)
            if userChoice == 1:
                userChoice = 'rock'
            elif userChoice == 2:
                userChoice = 'paper'
            elif userChoice == 3:
                userChoice = 'scissors'
            else:
                print("You did not input 1,2,or 3! Try again and input 1,2,or 3!")
        except ValueError:
            print("You did not input a number! Try again and input 1,2,or 3!")
        input("Press ENTER to get results")
        computerChoice = random.choice(choices)
        if userChoice == 'rock':
            if computerChoice == 'rock':
                print(f'You both did {userChoice}! Try again!')
            if computerChoice == 'paper':
                print(f'You lost to the computer :( They put {computerChoice}')
            if computerChoice == 'scissors':
                print(f'You won to the computer :) They put {computerChoice}')
        if userChoice == 'paper':
            if computerChoice == 'rock':
                print(f'You won to the computer :) They put {computerChoice}')
            if computerChoice == 'paper':
                print(f'You both did {userChoice}! Try again!')
            if computerChoice == 'scissors':
                print(f'You lost to the computer :( They put {computerChoice}')
        if userChoice == 'scissors':
            if computerChoice == 'rock':
                print(f'You lost to the computer :( They put {computerChoice}')
            if computerChoice == 'paper':
                print(f'You won to the computer :) They put {computerChoice}')
            if computerChoice == 'scissors':
                print(f'You both did {userChoice}! Try again!')