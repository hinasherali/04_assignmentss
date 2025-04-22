voting_ages = {  
    "Pakistan": 18,  
    "Turkey": 25,  
    "Iran": 48  
}  


age = int(input("How old are you? "))  

  
for country, voting_age in voting_ages.items():  
    if age >= voting_age:  
        print(f"You can vote in {country} where the voting age is {voting_age}.")  
    else:  
        print(f"You cannot vote in {country} where the voting age is {voting_age}.")  





