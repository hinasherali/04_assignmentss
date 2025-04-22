def feet_to_inches(feet):  
    """Convert feet to inches."""  
    inches = feet * 12    
    return inches  

def main():  
    while True:  
        user_input = input("Enter feet (type 'exit' to quit): ")  

        
        if user_input.lower() == 'exit':  
            print("Exiting the program.")  
            break  

        try:  
            
            feet = float(user_input)  

              
            inches = feet_to_inches(feet)  

             
            if feet == 1:  
                print(f"{feet} foot is {inches} inches.")  
            else:  
                print(f"{feet} feet is {inches} inches.")  

        except ValueError:  
            print("Please enter a valid number for feet.")  

 
if __name__ == "__main__":  
    main()  