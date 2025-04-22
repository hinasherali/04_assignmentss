import random  


DONE_LIKELIHOOD = 0.3  

def done():  
    """Return True with a likelihood defined by DONE_LIKELIHOOD."""  
    return random.random() < DONE_LIKELIHOOD  

def chaotic_counting():  
    """Count from 1 to 10, stopping if 'done()' returns True."""  
    for i in range(1, 11): 
        if done():  
            return  
        print(i, end=' ')  
     
    print() 

def main():  
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")  
    chaotic_counting() 
    print("I'm done.")  


if __name__ == "__main__":  
    main()  











    