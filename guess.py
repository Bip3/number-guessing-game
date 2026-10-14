from random import randint
import time

TIME_LIMIT = 60
DEBUG_SECRET = None
#DEBUG_SECRET = 42

#Setup section that exists outside the game loop
VALID_GAME_MODES = (1, 2)
DIFFICULTY_MAP = {1: 50, 2: 100, 3: 500}
ATTEMPTS_MAP = {1: 10, 2: 8, 3: 10}

#Game mode selection loop
def game_selection_loop():
    game_type = -1
    while True:
        game_type = input("Welcome to the advanced number guessing game! "
                          "Type the number of the game mode you would like to play:\n"
                          "1. Classic Mode\n2. Time Trial Mode\nInput: ")

        if game_type.isdigit() and int(game_type.lower().strip()) in VALID_GAME_MODES:
            game_type = int(game_type.lower().strip())
            break
        else:
            print("Invalid selection! Try again!\n\n")
    return game_type

#Difficulty selection loop
def difficulty_selection_loop():
    difficulty = -1
    while True:
        difficulty = input("Choose your desired difficulty:\n"
                           "1. Easy\n2. Medium\n3. Hard\nInput: ")
        difficulty = int(difficulty.lower().strip())
        if difficulty in DIFFICULTY_MAP.keys():
            break
        else:
            print("Invalid selection! Try again!\n\n")
        if difficulty.isdigit() and int(difficulty.lower().strip()) in DIFFICULTY_MAP.keys():
            difficulty = int(game_type.lower().strip())
            break
        else:
            print("Invalid selection! Try again!\n\n")
    return difficulty

#Classic Mode Loop. Takes in game parameters and begins a loop that tests user guesses.
def classic_mode(difficulty, max_attempts, random_number):
    attempts_remaining = max_attempts
    while attempts_remaining > 0:
        user_guess = input(f"You have {attempts_remaining} attempts left!\n"
                           "Guess the secret number: ")
        if not user_guess.isdigit():
            print("Invalid input! Try again!\n\n")
            continue
        user_guess = int(user_guess.lower().strip())
        if user_guess < 1 or user_guess >= DIFFICULTY_MAP[difficulty]:
            print("You guessed outside the allowed range! Try again!\n\n")
            continue
        if user_guess == random_number:
            print(f"You got it champ! Kudos. You had a {1/DIFFICULTY_MAP[difficulty] * 100}% chance to get it right!")
            break
        elif user_guess > random_number:
            print("Too high! Try again!\n\n")
        else:
            print("Too low! Try again!\n\n")
        attempts_remaining -= 1
    if attempts_remaining <= 0:
        print(f"You ran out of attempts! The secret number was {random_number} Try again!\n\n")

#Time Trial Loop
def time_challenge_mode(difficulty, max_attempts, random_number):
    attempts_remaining = max_attempts
    start_time = time.time()

    while attempts_remaining > 0:
        user_guess = input(f"You have {attempts_remaining} attempts left!\n"
                           f"With {TIME_LIMIT - int(time.time() - start_time)} seconds remaining\n\n"
                           "Guess the secret number: ")
        if not user_guess.isdigit():
            print("Invalid input! Try again!\n\n")
            continue
        user_guess = int(user_guess.lower().strip())
        if time.time() - start_time > TIME_LIMIT:
            print("You ran out of time! Try again!\n\n")
            break
        if user_guess < 1 or user_guess >= DIFFICULTY_MAP[difficulty]:
            print("You guessed outside the allowed range! Try again!\n\n")
            continue
        if user_guess == random_number:
            print(f"You got it champ! Kudos. You had a {1/DIFFICULTY_MAP[difficulty] * 100}% chance to get it right!")
            break
        elif user_guess > random_number:
            print("Too high! Try again!\n\n")
        else:
            print("Too low! Try again!\n\n")


        attempts_remaining -= 1
    if attempts_remaining <= 0:
        print(f"You ran out of attempts! The secret number was {random_number} Try again!\n\n")

#Game Setup: getting game type, difficulty, max attempts, and generating the random number
game_type = game_selection_loop()
difficulty = difficulty_selection_loop()
max_attempts = ATTEMPTS_MAP[difficulty]
if DEBUG_SECRET:
    random_number = DEBUG_SECRET
    print("The secret number is: ", random_number)
else:
    random_number = randint(1, DIFFICULTY_MAP[difficulty])

if game_type == 1:
    classic_mode(difficulty, max_attempts, random_number)
else:
    time_challenge_mode(difficulty, max_attempts, random_number)


