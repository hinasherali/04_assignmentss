def mad_libs():  
     
    adjective1 = input("Enter an adjective: ")  
    adjective2 = input("Enter another adjective: ")  
    noun1 = input("Enter a noun: ")  
    noun2 = input("Enter another noun: ")  
    verb1 = input("Enter a verb: ")  
    verb2 = input("Enter another verb: ")  
    place = input("Enter a place: ")  
    number = input("Enter a number: ")  
 
    story = f"""  
    Once upon a time in a {adjective1} land, there lived a {adjective2} {noun1}.   
    Every day, it would {verb1} to the {place}, carrying a small {noun2} with   
    {number} colorful stickers. One day, it decided to {verb2} to the magical forest,   
    and that's where the adventure began!  
    """  
 
    print(story)  

mad_libs()  