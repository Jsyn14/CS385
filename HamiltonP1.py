#Jayson Hamilton		
#jhamilt7@my.athens.edu
#00128552

"""
Time Converter Program
Converts seconds input into formatted time display showing days, hours, minutes, and seconds.
"""

def convert_seconds_to_time(total_seconds):
    """
    Convert total seconds to days, hours, minutes, and remaining seconds.
    
    Args:
        total_seconds (int): Total number of seconds to convert
        
    Returns:
        tuple: (days, hours, minutes, seconds)
    """
    # Constants for time conversion
    SECONDS_PER_DAY = 86400    # 24 * 60 * 60
    SECONDS_PER_HOUR = 3600    # 60 * 60
    SECONDS_PER_MINUTE = 60
    
    # Calculate days and remaining seconds
    days = total_seconds // SECONDS_PER_DAY
    remaining_seconds = total_seconds % SECONDS_PER_DAY
    
    # Calculate hours and remaining seconds
    hours = remaining_seconds // SECONDS_PER_HOUR
    remaining_seconds = remaining_seconds % SECONDS_PER_HOUR
    
    # Calculate minutes and remaining seconds
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    
    return days, hours, minutes, seconds

def format_time_display(days, hours, minutes, seconds):
    """
    Format the time components into a readable string.
    Only shows relevant time units (skips units that are 0 from the left).
    
    Args:
        days (int): Number of days
        hours (int): Number of hours
        minutes (int): Number of minutes
        seconds (int): Number of seconds
        
    Returns:
        str: Formatted time string
    """
    time_parts = []
    
    # Add days if present
    if days > 0:
        time_parts.append(f"{days} day{'s' if days != 1 else ''}")
    
    # Add hours if present or if we have days
    if hours > 0 or days > 0:
        time_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    
    # Add minutes if present or if we have hours/days
    if minutes > 0 or hours > 0 or days > 0:
        time_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    
    # Always show seconds
    time_parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return ": ".join(time_parts)

def get_valid_seconds_input():
    """
    Get valid seconds input from user with input validation.
    
    Returns:
        int: Valid number of seconds (non-negative integer)
    """
    while True:
        try:
            user_input = input("Enter the number of seconds: ").strip()
            
            # Check for empty input
            if not user_input:
                print("Error: Please enter a number.")
                continue
            
            # Convert to integer
            seconds = int(user_input)
            
            # Check for negative numbers
            if seconds < 0:
                print("Error: Please enter a non-negative number.")
                continue
            
            return seconds
            
        except ValueError:
            print("Error: Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            exit(0)
        except EOFError:
            print("\nEnd of input reached. Exiting...")
            exit(0)

def main():
    """
    Main function to run the time converter program.
    """
    print("=" * 50)
    print("Time Converter - Seconds to Days:Hours:Minutes:Seconds")
    print("=" * 50)
    print()
    
    try:
        # Get user input
        total_seconds = get_valid_seconds_input()
        
        # Convert seconds to time components
        days, hours, minutes, seconds = convert_seconds_to_time(total_seconds)
        
        # Format and display the result
        formatted_time = format_time_display(days, hours, minutes, seconds)
        
        print()
        print("Result:")
        print("-" * 20)
        print(f"Input: {total_seconds} seconds")
        print(f"Output: {formatted_time}")
        
        # Also show the breakdown for clarity
        print()
        print("Breakdown:")
        print(f"• Days: {days}")
        print(f"• Hours: {hours}")
        print(f"• Minutes: {minutes}")
        print(f"• Seconds: {seconds}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    # Run the program multiple times if user wants to continue
    while True:
        exit_code = main()
        
        if exit_code != 0:
            break
        
        print("\n" + "=" * 50)
        
        try:
            continue_choice = input("\nWould you like to convert another time? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Time Converter!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nThank you for using the Time Converter!")
            break
        
        print()
