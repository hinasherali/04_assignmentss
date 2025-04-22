def get_user_data():  
    """  
    Prompts the user for their first name, last name, and email address,  
    and returns them as a tuple.  
    """  
    first_name = input("What is your first name?: ")  
    last_name = input("What is your last name?: ")  
    email = input("What is your email address?: ")  
    
    return first_name, last_name, email  

def main():  
    
    user_data = get_user_data()  
     
    print(f"Received the following user data: {user_data}")  

  
if __name__ == "__main__":  
    main()  






    