
initial_value = float(input("Enter a number: "))  

 
curr_value = initial_value  


results = []  

 
while curr_value < 100:  
    curr_value *= 2  
    results.append(str(int(curr_value)))  


print(" ".join(results))  








