import math  

def main():  
      
    try:  
        ab = float(input("Enter the length of AB: "))  
        ac = float(input("Enter the length of AC: "))  

        
        bc = math.sqrt(ab**2 + ac**2)  

        
        print(f"The length of BC (the hypotenuse) is: {bc:.1f}")  

    except ValueError:  
        print("Please enter valid numeric values for the lengths.")  

 
if __name__ == "__main__":  
    main()  


    