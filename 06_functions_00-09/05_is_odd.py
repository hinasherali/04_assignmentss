def even_odd_sequence(start, end):  
    result = []  
    for num in range(start, end + 1):  
        if num % 2 == 0:  
            result.append(f"{num} even")  
        else:  
            result.append(f"{num} odd")  
    return ' '.join(result)  

def main():  
    start = 10  
    end = 19  
    output = even_odd_sequence(start, end)  
    print(output)  

if __name__ == "__main__":  
    main()  








    