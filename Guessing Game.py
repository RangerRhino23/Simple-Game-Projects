import random


if __name__ == '__main__':
    while True:
        min = 0
        max = 100
        input("Press ENTER to generate the random number ")
        computerNum = random.randint(min,max)
        tries = 0
        
        while True:
            userGuess = input(f'Guess a number between {min}-{max}: ')
            try:
                userGuess = int(userGuess)
                tries += 1
            except ValueError:
                print("You did not input a number! Try again and input a number")
                continue
            if userGuess > computerNum:
                print('Your number is higher than the computer number...')
            elif userGuess < computerNum:
                print('Your number is lower than the computer number...')
            elif userGuess == computerNum:
                print(f"You got it in {tries} tries!")
                input("Press ENTER to play again...")
                break