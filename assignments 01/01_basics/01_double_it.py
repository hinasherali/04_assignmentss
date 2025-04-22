def main():  
     
    user_input = input("Enter a number: ")  
    curr_value = int(user_input)  

     
    results = []  

    
    while curr_value < 100:  
        curr_value *= 2  
        results.append(curr_value)   

     
    print(" ".join(map(str, results)))  


if __name__ == "__main__":  
    main()  




    