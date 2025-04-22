number_counts = {}  

  
while True:  
    user_input = input("Enter a number: ")  
    
   
    if user_input == "":  
        break  
    
   
    try:  
        number = int(user_input)  
        
       
        if number in number_counts:  
            number_counts[number] += 1  
        else:  
            number_counts[number] = 1  
    except ValueError:  
        print("Please enter a valid integer.")  


for number, count in number_counts.items():  
    print(f"{number} appears {count} times.")  








    