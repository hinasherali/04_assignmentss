 def is_leap_year(year):  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
        return True  
    else:  
        return False  

 
year = int(input("Please enter a year: "))  

  
if is_leap_year(year):  
    print("That's a leap year!")  
else:  
    print("That's not a leap year.")  





    