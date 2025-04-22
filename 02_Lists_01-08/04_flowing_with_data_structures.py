def add_three_copies(my_list, data):  
    """Add three copies of 'data' to 'my_list'."""  
    my_list.append(data)    
    my_list.append(data)   
    my_list.append(data)  

def main():  
    
    user_input = input("Enter a message to copy: ")  
    
    
    message_list = []  
    
   
    print(f"List before: {message_list}")  
    
     
    add_three_copies(message_list, user_input)  
    
     
    print(f"List after: {message_list}")  

if __name__ == "__main__":  
    main()  








    