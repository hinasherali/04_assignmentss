import hashlib  

 
def hash_password(password):  
    return hashlib.sha256(password.encode()).hexdigest()  

 
stored_logins = {  
    "user@example.com": hash_password("password123"),  
    "admin@example.com": hash_password("adminpass")  
}  

def login(email, password_to_check):  
   
    hashed_password = hash_password(password_to_check)  
    
    
    if email in stored_logins and stored_logins[email] == hashed_password:  
        return True  
    else:  
        return False  

 
if __name__ == "__main__":  
    email_input = input("Enter your email: ")  
    password_input = input("Enter your password: ")  

    if login(email_input, password_input):  
        print("Login successful!")  
    else:  
        print("Login failed. Please check your email and password.")  








        