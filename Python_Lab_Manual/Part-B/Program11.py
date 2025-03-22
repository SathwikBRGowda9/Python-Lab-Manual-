#Demonstrate Exception Handling 
try:
    # Prompt user for input
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Perform division
    result = numerator / denominator
    print(f"The result is {result}")
    
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    # Handle invalid input
    print("Error: Please enter a valid number.")
    
finally:
    # Code that runs no matter what
    print("Program execution completed.")
