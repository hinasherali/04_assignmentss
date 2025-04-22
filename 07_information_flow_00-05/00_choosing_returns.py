ADULT_AGE = 18  

def is_adult(age):  
    return age >= ADULT_AGE  
  
age_input = int(input("How old is this person?: "))  
print(is_adult(age_input))  



