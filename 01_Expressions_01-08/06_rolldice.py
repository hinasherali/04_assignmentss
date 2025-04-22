import random  

def roll_dice():  
    """Simulate rolling two dice and return their values."""  
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)   
    return die1, die2  

def main():  
   
    die1, die2 = roll_dice()  
    
   
    total = die1 + die2  
    
   
    print(f"Results of the rolls:")  
    print(f"Die 1: {die1}")  
    print(f"Die 2: {die2}")  
    print(f"Total: {total}")  

 
if __name__ == "__main__":  
    main()  







    