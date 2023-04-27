import random


if __name__ == '__main__':
    while True:
        input("Press ENTER to generate the random number ")
        computerNum = random.randint(0,100)
        tries = 0
        
        while True:
            userGuess = input('Guess a number between 1-100: ')
            try:
                userGuess = int(userGuess)
            except ValueError:
                print("You did not input a number! Try again and input a number")
                continue
            if userGuess > computerNum:
                print('Your number is higher than the computer number...')
                tries += 1
            elif userGuess < computerNum:
                print('Your number is lower than the computer number...')
                tries += 1
            elif userGuess == computerNum:
                print(f"You got it in {tries} tries!")
                input("Press ENTER to play again...")
                break