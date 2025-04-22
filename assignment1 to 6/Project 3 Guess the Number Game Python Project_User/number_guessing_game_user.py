import random

def main():
    print("Welcome to the Number Guessing Game!")

    user1_name = input("User 1, please enter your name: ")
    user1_number = int(input(f"{user1_name}, please choose a number between 1 and 100 (inclusive): "))

    if user1_number < 1 or user1_number > 100:
        print("Number must be between 1 and 100. Game over.")
        return

    user2_name = input("User 2, please enter your name: ")
    print(f"Okay, {user2_name}, try to guess the number chosen by {user1_name}!")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Your guess is out of bounds. Please guess a number between 1 and 100.")
            elif guess < user1_number:
                print("Too low! Try again.")
            elif guess > user1_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations, {user2_name}! You've guessed the number {user1_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()