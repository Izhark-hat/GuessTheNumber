import random


def guess(x):
    random_number = random.randint(1, x)

    guess: int = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'woo, congratulations. You have guessed the right number {random_number} correctly!!')


guess(100)
