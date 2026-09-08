#We implement a number guessing game

import random

def play_game(num_to_guess, mode):
    chosen_mode = str(mode)
    if chosen_mode == 'easy':
        end_range = 9
        print("You have 9 attempts to guess the number.\n")
    else:
        end_range = 5
        print("You have 5 attempts to guess the number.\n")
    for x in range(1,end_range + 1):
        guess = int(input("Guess the number: \n"))
        if guess == num_to_guess:
            print("Congratulations! You guessed the number!\n")
            break
        else:
            if guess < num_to_guess:
                print("Your guess is too low.\n")
            else:
                print("Your guess is too high.\n")
            if x == end_range:
                print(f"Sorry, you're out of attempts. The number was {num_to_guess}.\n")


def main():
    print("Welcome to the our Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    number_to_guess = random.randint(1, 100)
    game_mode = input("Choose your level. (\"easy\" or \"hard\")\n")
    while game_mode != "easy" and game_mode != "hard":
        print("Invalid choice.\n")
        game_mode = input("Choose your level. (\"easy\" or \"hard\")\n")
    play_game(number_to_guess, game_mode)
    print("Thank you for playing!\n")


main()