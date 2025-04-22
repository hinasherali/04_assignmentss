def shorten(lst):  
    """Remove elements from the end of the list until it is MAX_LENGTH items long."""  
    MAX_LENGTH = 3  
    while len(lst) > MAX_LENGTH:  
        removed_element = lst.pop()    
        print(f"Removing: {removed_element}")  

def main():  
    
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']  
    
    print(f"Original list: {lst}")  
    shorten(lst)   
    print(f"Shortened list: {lst}")  

if __name__ == "__main__":  
    main()  





    