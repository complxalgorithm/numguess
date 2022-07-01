# Name: numguess.py
#
# Author: Stephen C Sanders <https://stephensanders.me>
#
# Description: Generates a random number between 1 and a randomly determined end interval between 50 and 100, and allows the user to
# guess the number until they are correct. If the guess is incorrect, the program will give a hint as to whether the guess was too high or low.
# Once user guesses correctly, program will output the number of guesses it took, some facts about the number, and what the user's best try was.
# After each game, program asks user if they would like to continue playing. If so, then another random number is generated between 1 and another
# randomly determined end interval between 50 and 100 and the user tries to guess that number.
# Program keeps track of, or calculates: number of guesses that the user made for each game, the total number of guesses that the user
# made while the program was running, the number of games played, the average number of guesses per game, the user's lowest number of
# guesses, the exact game that the user did their best on, and how many times the user matched their best try.
# Program does not end until user inputs that they don't want to play anymore. Once the user signals that they are done, the program
# will output statistics relevant to the user's time playing the game.

import random                      # Required to use randint()

def main():
    # Initialize variables
    cont_status = 'Y'              # Used to ask user if they want to continue playing
    num_guesses = 0                # Used to keep track of the number of guesses
    tot_guesses = 0                # Used to keep track of number of total guesses by user since they started playing
    best_num_guesses = 0           # Used to keep track of the lowest number of guesses
    user_guess = 0                 # Used to store the user's guess
    times_played = 0               # Used to keep track of how many times the user played the game
    best_game = 0                  # Used to determine the game where user did their best
    num_best_games = 1             # Used to count number of times user matches best number of guesses

    # Opening prompts
    print('Welcome to the Number Guessing Game!')
    print('I will pick a number within a determined interval, and then you will guess until you get it correct.')
    input('Click Enter to continue...')
    
    # Keep playing until user inputs that they no longer want to play
    while cont_status == 'Y' or cont_status == 'y':
        # Determine end interval for range of possible numbers
        range_limit = get_rand_limit()
        
        # Determine the number to guess
        num = get_rand_num(range_limit)

        print(f'I have chosen a number between 1 and {range_limit}.')
        
        # Have user keep guessing until they guess the number correctly
        while user_guess != num:
            # Ask user for guess
            user_guess = input('Enter your guess: ')

            # Validate that input is a positive number
            while not(user_guess.isdigit()):
                # Had to specify "negative number" since this loop interprets negative numbers as non-numbers
                print('ERROR: Input is either a negative number or a non-number. Try again.')
                user_guess = input('Enter your guess: ')

            # Convert user guess to int
            user_guess = int(user_guess)

            # Nested validation loop - range and isdigit()
            while user_guess < 1 or user_guess > range_limit:  # Validate that guess is within range
                print(f'ERROR: Number is not between 1 and {range_limit}. Try again.')
                user_guess = input('Enter your guess: ')
                
                while not(user_guess.isdigit()):  # Validate that any new input is a positive number
                    print('ERROR: Input is either a negative number or non-number. Try again.')
                    user_guess = input('Enter your guess: ')
                
                user_guess = int(user_guess)  # Convert valid user guess to int
            
            num_guesses += 1 # Add 1 to number of guesses
            tot_guesses += 1 # Add 1 to number of total guesses

            # Give user a hint if wrong, or congratulate if correct
            if user_guess < num:
                print('Your guess is too low. Try again.')
            elif user_guess > num:
                print('Your guess is too high. Try again')
            else:
                print('Congratulations, you\'re correct!')

        # Reinitialize user_guess
        user_guess = 0  # The next game's random number could be the same as the last correct guess, which forced the program to skip to code below

        # Display whether random number is even or odd, and if it is divisible by 10
        if (num % 2) == 0:  # If even
            print(f'Fun facts: {num} is an even integer, and', end = ' ')
        else:
            print(f'Fun facts: {num} is an odd number, and', end = ' ')

        if (num % 5) == 0:  # If divisible by 5
            print('is also divisible by 5.')
        else:
            print('is not divisible by 5.')
        
        # Display number of guesses it took to guess the correct number
        print(f'It took you {num_guesses} guesses to get the right number.')

        # Add 1 to number of games played
        times_played += 1

        # Determine if number of guesses was the best
        if num_guesses < best_num_guesses or best_num_guesses == 0:
            best_num_guesses = num_guesses # Updates best number of guesses (lower than previous best)
            best_game = times_played       # Updates the game that is user's best
            num_best_games = 1             # Resets number of best games to 1
            print('That\'s your best try so far!')
        elif num_guesses > best_num_guesses:
            print(f'Your best is {best_num_guesses} guesses.')
        else:
            num_best_games += 1   # Add 1 to number of times user tied best number of guesses
            print(f'You tied your best of {best_num_guesses} guesses!')

        # Reset number of guesses
        num_guesses = 0

        # Determine if user wants to play again
        cont_status = get_continue_status()

    avg_guesses = float(tot_guesses / times_played) # Determine average number of guesses per game
    
    print(f'You made a total of {tot_guesses} guesses in your {times_played} games.')
    print(f'You averaged {avg_guesses:.2f} guesses per game played.')
    if num_best_games == 1:  # When user only has one best try, output on which game it occurred
        print(f'Your best try was on Game {best_game}, when you only had to guess {best_num_guesses} times.')
    else:                    # When user gets best try multiple times, output how many times instead of the exact games that they did their best
        print(f'Your best try was when you took only {best_num_guesses} times to guess correctly, which you achieved in {num_best_games} games.')
    print('Thank you for playing the Number Guessing Game! I will see you next time.')

# Generates random number range limit between 50 and 100
def get_rand_limit():
    rand_lim = random.randint(50, 100)  # Generates random number between 50 and 100
    return rand_lim

# Generates random number to guess between 1 and the range limit
def get_rand_num(limit):
    rand_int = random.randint(1, limit) # Generates random number between 1 and the number limit
    return rand_int

# User's status on desire to play again
def get_continue_status():
    # Get user's answer
    inp = input('Would you like to play again? Y or N\n')

    # If uppercase version of answer is either 'Y' or 'N', then that is valid input
    if inp.upper() in ('Y', 'N'):
        return inp
    else:
        print('ERROR: Invalid answer.')
        return get_continue_status()    # Loop back to beginning of function

# Execute the main function
main()
