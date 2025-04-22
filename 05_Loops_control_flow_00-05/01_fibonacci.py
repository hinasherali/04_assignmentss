 
MAX_FIB = 10000  

def fibonacci_sequence(max_value):  
    
    a, b = 0, 1  
    fibonacci_numbers = []  
    
     
    while a < max_value:  
        fibonacci_numbers.append(a) 
        a, b = b, a + b  

    return fibonacci_numbers  


fib_numbers = fibonacci_sequence(MAX_FIB)  
print(" ".join(map(str, fib_numbers)))  







