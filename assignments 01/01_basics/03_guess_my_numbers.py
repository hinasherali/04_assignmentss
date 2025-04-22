import random  

def main():  
     
    secret_number = random.randint(0, 99)  
    print("I am thinking of a number between 0 and 99...")  

    guess = -1  

    
    while guess != secret_number:  
     
        guess = int(input("Enter a guess: "))  

     
        if guess < secret_number:  
            print("Your guess is too low.")  
        elif guess > secret_number:  
            print("Your guess is too high.")  

    
    print(f"Congrats! The number was: {secret_number}")  


if __name__ == "__main__":  
    main()  






    