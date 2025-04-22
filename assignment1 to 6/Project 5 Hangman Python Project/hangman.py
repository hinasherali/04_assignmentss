import random  

def choose_word():  
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']  
    return random.choice(words)  

def display_hangman(tries):  
    stages = [  
        """  
           -----  
           |   |  
           |   O  
           |  /|\\
           |  / \\
           |  
        """,  
        """  
           -----  
           |   |  
           |   O  
           |  /|\\
           |  /  
           |  
        """,  
        """  
           -----  
           |   |  
           |   O  
           |  /|\\
           |  
           |  
        """,  
        """  
           -----  
           |   |  
           |   O  
           |   |  
           |  
           |  
        """,  
        """  
           -----  
           |   |  
           |   O  
           |  
           |  
           |  
        """,  
        """  
           -----  
           |   |  
           |  
           |  
           |  
           |  
        """,  
        """  
           -----  
           |   |  
           |  
           |  
           |  
           |  
        """,  
    ]  
    return stages[tries]  

def play_hangman():  
    word = choose_word()  
    word_letters = set(word)  
    used_letters = set()  
    tries = 6  
    print("Welcome to Hangman!")  

    while tries > 0:  
        print(display_hangman(tries))  
        print(f"Used letters: {' '.join(sorted(used_letters))}")  
        word_display = [letter if letter in used_letters else '_' for letter in word]  
        print("Word to guess: " + " ".join(word_display))  

        # Check if the player has won  
        if word_letters.issubset(used_letters):  
            print(f"Congratulations! You guessed the word: '{word}'.")  
            break  

        guess = input("Guess a letter: ").lower()  

        if len(guess) != 1 or not guess.isalpha():  
            print("Please enter a single alphabetical letter.")  
            continue  

        if guess in used_letters:  
            print("You've already guessed that letter. Try again.")  
            continue  

        used_letters.add(guess)  

        if guess in word_letters:  
            print(f"Good guess! '{guess}' is in the word.")  
            word_letters.remove(guess)  
        else:  
            print(f"Sorry, '{guess}' is not in the word.")  
            tries -= 1  

    if tries == 0:  
        print(display_hangman(tries))  
        print(f"You lost! The word was '{word}'.")  

if __name__ == "__main__":  
    play_hangman()  