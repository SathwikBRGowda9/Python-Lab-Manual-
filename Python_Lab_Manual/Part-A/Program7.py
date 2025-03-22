#7.	Explore String Functions

text = "Hello World"
slice_1 = text[0:5]     # 'Hello'
slice_2 = text[6:]      # 'World'
slice_3 = text[::2]     # 'HloWrd'
print(slice_1)
print(slice_2)
print(slice_3)

# User Input Program with String Functions
name = input("Enter your full name: ").strip()
greeting = "Hello"

# Apply String Functions
# 1. Title Case the Name
formatted_name = name.title()

# 2. Combine the Greeting with the Name
message = f"{greeting}, {formatted_name}!"

# 3. Check for Specific Conditions
contains_space = " " in name  # Check if the input contains spaces (full name)

# 4. Reverse the Name
reversed_name = name[::-1]

# 5. Count the Occurrences of a Letter (e.g., 'a')
letter_count = name.lower().count('a')

# Print the Results
print("\n--- String Functions Example ---")
print("Formatted Name:", formatted_name)
print("Greeting Message:", message)
print("Contains Space:", contains_space)
print("Reversed Name:", reversed_name)
print(f"Occurrences of 'a': {letter_count}")
