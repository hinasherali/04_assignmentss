def main():  
      
    planet_gravity = {  
        "Mercury": 0.376,  
        "Venus": 0.889,  
        "Mars": 0.378,  
        "Jupiter": 2.36,  
        "Saturn": 1.081,  
        "Uranus": 0.815,  
        "Neptune": 1.14  
    }  

     
    weight_on_earth = float(input("Enter a weight on Earth: "))  
    
    
    planet = input("Enter a planet: ")  

    
    if planet in planet_gravity:  
        weight_on_planet = weight_on_earth * planet_gravity[planet]  
        print(f"The equivalent weight on {planet}: {round(weight_on_planet, 2)}")  
    else:  
        print("Sorry, the planet is not recognized.")  

 
if __name__ == "__main__":  
    main()  