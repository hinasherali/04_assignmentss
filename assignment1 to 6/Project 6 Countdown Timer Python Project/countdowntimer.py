import time  
import threading  

running = True  

def countdown_timer(seconds):  
    global running  
    try:  
        while seconds and running:  
            mins, secs = divmod(seconds, 60)  
            timer = '{:02d}:{:02d}'.format(mins, secs)  
            print(timer, end='\r')   
            time.sleep(1)  
            seconds -= 1  

        if running: 
            print("Time's up!")  
    except Exception as e:  
        print(f"An error occurred: {e}")  

def wait_for_exit():  
    input("Press Enter to exit the timer...")  
    global running  
    running = False   

if __name__ == "__main__":  
    total_seconds = int(input("Enter the time in seconds: "))  
    timer_thread = threading.Thread(target=countdown_timer, args=(total_seconds,))  
    timer_thread.start()  
     
    wait_for_exit()  
    
    timer_thread.join()  
    print("\nExiting the timer...")  
    print("Goodbye!")