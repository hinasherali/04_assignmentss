def calculate_average(num1, num2):  
    """Calculate the average of two numbers."""  
    average = (num1 + num2) / 2  
    return average  

 
if __name__ == "__main__":  
     
    number1 = float(input("Enter the first number: "))  
    number2 = float(input("Enter the second number: "))  
 
    average_result = calculate_average(number1, number2)  
    print(f"The average of {number1} and {number2} is: {average_result}")  






    