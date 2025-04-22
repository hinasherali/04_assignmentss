def main():  
    
    C = 299792458  

    while True:  
      
        user_input = input("Enter kilos of mass (type 'exit' to quit): ")  

     
        if user_input.lower() == 'exit':  
            print("Exiting the program.")  
            break  

        try:  
            
            mass = float(user_input)  

              
            energy = mass * (C ** 2)  

          
            print(f"\ne = m * C^2...\n")  
            print(f"m = {mass} kg")  
            print(f"C = {C} m/s")  
            print(f"{energy} joules of energy!\n")  

        except ValueError:  
            print("Please enter a valid number for mass.")  

 
if __name__ == "__main__":  
    main()  