def get_last_element(lst):  
    """Print the last element of the list."""  
    print(f"The last element is: {lst[-1]}")   

def main():  
      
    num_elements = int(input("How many elements do you want to input? "))  
    
   
    lst = []  
    
     
    for i in range(num_elements):  
        element = input(f"Enter element {i + 1}: ")  
        lst.append(element)  

    
    get_last_element(lst)  

if __name__ == "__main__":  
    main()  









    