import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    attempts = 0
    while True:
        try:
            user_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:  
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
   number_guessing_game()
