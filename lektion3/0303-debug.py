import random

random_number = random.randint(1, 200)

guess = 0

while guess != random_number:
    guess = int(input("Guess the number (1-200): "))

    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")