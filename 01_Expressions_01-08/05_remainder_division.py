def main():  
    try:  
        
        dividend = int(input("Please enter an integer to be divided: "))  
        
     
        divisor = int(input("Please enter an integer to divide by: "))  

       
        if divisor == 0:  
            print("Error: Division by zero is not allowed.")  
            return  

        
        quotient = dividend // divisor   
        remainder = dividend % divisor   

         
        print(f"The result of this division is {quotient} with a remainder of {remainder}.")  

    except ValueError:  
        print("Please enter valid integers.")  
  
if __name__ == "__main__":  
    main()  











































