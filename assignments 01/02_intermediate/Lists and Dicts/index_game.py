def access_element(lst, index):  
    """Returns the element at the specified index or a message if out of range."""  
    if index < 0 or index >= len(lst):  
        return "Index out of range."  
    return lst[index]  

def modify_element(lst, index, new_value):  
    """Replaces the element at the specified index with the new value."""  
    if index < 0 or index >= len(lst):  
        return "Index out of range."  
    lst[index] = new_value  
    return lst  

def slice_list(lst, start, end):  
    """Returns a new list by slicing from start to end index."""  
    if start < 0 or end > len(lst) or start > end:  
        return "Index out of range."  
    return lst[start:end]  

def index_game():  
    """Simple text-based game for list manipulation."""  
    my_list = [10, 'hello', 3.14, 'world', 42]  
    print("Welcome to the Index Game! You can access, modify, or slice a predefined list.") 
    print("Initial list:", my_list)  
    
    while True:  
        operation = input("Choose an operation - 'access', 'modify', 'slice', or 'exit': ").strip().lower()  

        if operation == 'exit':  
            print("Thank you for playing! Exiting the game. Goodbye!")  
            break  

        if operation == 'access':  
            index = int(input("Enter the index to access: "))  
            result = access_element(my_list, index)  
            print("Accessed element:", result)  

        elif operation == 'modify':  
            index = int(input("Enter the index to modify: "))  
            new_value = input("Enter the new value: ")  
            result = modify_element(my_list, index, new_value)  
            print("Updated list:", result)  

        elif operation == 'slice':  
            start = int(input("Enter the start index: "))  
            end = int(input("Enter the end index: "))  
            result = slice_list(my_list, start, end)  
            print("Sliced list:", result)  

        else:  
            print("Invalid operation. Please choose again.")  


if __name__ == "__main__":  
    index_game()  