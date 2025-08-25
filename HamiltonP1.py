# Jayson Hamilton		
# jhamilt7@my.athens.edu
# 00128552
# Assisted by Replit

# Time Converter Program
# Converts seconds into days, hours, minutes, and seconds

print("Time Converter Program")

answer = "y"
while answer == "y":
    # Get input from user
    s = int(input("Enter the number of seconds: "))
    
    # Calculate days
    d = s // 86400
    s = s % 86400
    
    # Calculate hours
    h = s // 3600
    s = s % 3600
    
    # Calculate minutes
    m = s // 60
    s = s % 60
    
    # Print the result
    if d > 0:
        print(d, "days:", h, "hours:", m, "minutes:", s, "seconds")
    elif h > 0:
        print(h, "hours:", m, "minutes:", s, "seconds")
    elif m > 0:
        print(m, "minutes:", s, "seconds")
    else:
        print(s, "seconds")
    
    # Ask if user wants to continue
    answer = input("Do you want to convert another time? (y/n): ")

print("Goodbye!")
