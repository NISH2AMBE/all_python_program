import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Guess Your Number Beetwin 1 To 100:--> "))
game_over = False

while not game_over:
    if winning_number == number:
        print(f"You Win, And Your Guess Time {guess}")
        game_over = True

    else:
        if number < winning_number:
            print("Too less")
            guess += 1
            number = int(input("Try again :--> "))
        else:
            print("Too high")
            guess += 1
            number = int(input("Try again :--> "))

