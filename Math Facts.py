import random

def addition():
    while True:
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        response = input(f'{num1}+{num2}=')
        if response == 'exit':
            quit()
        try:
            response = int(response)
            if response == int(num1+num2):
                input(f"Correct! The answer to {num1}+{num2}={response}. Press ENTER to continue ")
            else:
                input(f'Incorrect. The answer to {num1}+{num2}={num1+num2} not {response}. Press ENTER to continue')
        except ValueError:
                print("You need to input a number. Try again")

def subtraction():
    while True:
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        response = input(f'{num1}-{num2}=')
        if response == 'exit':
            quit()
        try:
            response = int(response)
            if response == int(num1-num2):
                input(f"Correct! The answer to {num1}-{num2}={response}. Press ENTER to continue ")
            else:
                input(f'Incorrect. The answer to {num1}-{num2}={num1-num2} not {response}. Press ENTER to continue')
        except ValueError:
                print("You need to input a number. Try again")

def multiplication():
    while True:
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        response = input(f'{num1}x{num2}=')
        if response == 'exit':
            quit()
        try:
            response = int(response)
            if response == int(num1*num2):
                input(f"Correct! The answer to {num1}x{num2}={response}. Press ENTER to continue ")
            else:
                input(f'Incorrect. The answer to {num1}x{num2}={num1*num2} not {response}. Press ENTER to continue')
        except ValueError:
                print("You need to input a number. Try again")

if __name__=='__main__':
    while True:
        option = input("What Math Facts do you want to Study? \n(1. Addition, 2. Subtraction, 3. Multiplication) ")
        try:
            option = int(option)
            if option == 1:
                addition()
            if option == 2:
                subtraction()
            if option == 3:
                multiplication()
            else:
                print("You need to put 1, 2, or 3. Try again")
        except ValueError:
            print("You need to input a number. Try again")