from random import randint

if __name__ == '__main__':
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
    win_number = randint(1, 99)
    tries = 1
    while True:
        print("What's your guess between 1 and 99?")
        number = input(">> ")
        if (number == "exit"):
            print("Goodbye!")
            break
        elif number.isdigit():
            number = int(number)
            if number > win_number:
                print('Too high!')
            elif number < win_number:
                print("Too low!")
            elif number == win_number:
                if tries == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("""Congratulations, you've got it!
You won in {} attempts!""".format(tries))
                break
        else:
            print("That's not a number.")
        tries += 1
