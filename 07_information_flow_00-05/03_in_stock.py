  inventory = {  
    "apple": 50,  
    "banana": 200,  
    "pear": 1000,  
    "orange": 0,  
    "grape": 300  
}  

def num_in_stock(fruit):  
    """  
    Returns the number of the specified fruit in stock.  
    If the fruit is not found in the inventory, returns 0.  
    """  
    return inventory.get(fruit.lower(), 0) 

def main():  
     
    fruit = input("Enter a fruit: ")  
    
     
    count = num_in_stock(fruit)  
    
     
    if count > 0:  
        print(f"This fruit is in stock! Here is how many:\n{count}")  
    else:  
        print("This fruit is not in stock.")  

 
if __name__ == "__main__":  
    main()  





    