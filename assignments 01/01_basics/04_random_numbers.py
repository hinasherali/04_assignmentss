import random  

def main():  
    
    random_numbers = [random.randint(1, 100) for _ in range(10)]  
    print(" ".join(map(str, random_numbers)))  

 
if __name__ == "__main__":  
    main()  




    