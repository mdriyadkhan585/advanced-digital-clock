import time
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    """Displays a welcome message."""
    print("======================================")
    print("      Welcome to the Digital Clock    ")
    print("======================================\n")
    print("Press Ctrl+C to exit the program.\n")

def display_clock():
    """Displays the clock with the current date and time."""
    while True:
        # Get the current local time
        local_time = time.localtime()
        
        # Determine AM or PM
        am_pm = "PM" if local_time.tm_hour >= 12 else "AM"

        # Convert to 12-hour format
        hour = local_time.tm_hour % 12
        if hour == 0:
            hour = 12

        # Clear the screen
        clear_screen()
        
        # Print the welcome message
        print_welcome_message()

        # Print the date and time in a formatted way
        print("Current Date and Time:")
        print("======================================")
        print(f"  Date: {local_time.tm_mday:02d}-{local_time.tm_mon:02d}-{local_time.tm_year}")
        print(f"  Time: {hour:02d}:{local_time.tm_min:02d}:{local_time.tm_sec:02d} {am_pm}")
        print("======================================")
        
        # Sleep for 1 second before updating the time
        time.sleep(1)

if __name__ == "__main__":
    try:
        display_clock()
    except KeyboardInterrupt:
        print("\nClock exited.")
      
