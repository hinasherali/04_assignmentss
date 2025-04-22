def double_numbers(numbers):  
    """Return a new list with each element doubled."""  
    doubled_list = [num * 2 for num in numbers] 
    return doubled_list  

 
if __name__ == "__main__":  
     
    numbers = [1, 2, 3, 4]  
    
     
    doubled_numbers = double_numbers(numbers)  
    
    
    print(f"Original list: {numbers}")  
    print(f"Doubled list: {doubled_numbers}")  




















    