MIN_HEIGHT = 50  

def tall_enough_extension():  
    while True:  
       
        height_input = input("How tall are you? (Press Enter to stop) ")  
        
       
        if height_input == "":  
            print("Thank you for using the height checker. Goodbye!")  
            break  
        
       
        try:  
            height = int(height_input)  
         
            if height >= MIN_HEIGHT:  
                print("You're tall enough to ride!")  
            else:  
                print("You're not tall enough to ride, but maybe next year!")  
        except ValueError:  
            print("Please enter a valid number.")  

  
tall_enough_extension()  










