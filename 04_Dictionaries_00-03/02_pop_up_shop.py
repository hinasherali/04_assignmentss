
fruits = {  
    "apple": 0.5,  
    "durian": 2.5,  
    "jackfruit": 1.5,  
    "kiwi": 1.0,  
    "rambutan": 2.0,  
    "mango": 1.5  
}  

def calculate_total_cost(fruits):  
    total_cost = 0.0  
    
    
    for fruit, price in fruits.items():  
        
        quantity = int(input(f"How many ({fruit}) do you want?: "))  
        total_cost += quantity * price  
    
    return total_cost  

def main():  
    total = calculate_total_cost(fruits)  
    print(f"\nYour total is ${total:.2f}")  

 
if __name__ == "__main__":  
    main()  








    