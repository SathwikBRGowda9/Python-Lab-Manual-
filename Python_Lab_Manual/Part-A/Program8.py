#8.	Read and Write into File 

# File Read and Write Example

# Step 1: Write to a file
file_name = "example.txt"

# Open the file in write mode
with open(file_name, "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to file handling in Python.\n")

print("Data written to file successfully.")

# Step 2: Read from the file
print("\nReading from the file:")
with open(file_name, "r") as file:
    content = file.read()

# Display the file content
print(content)

# Step 3: Append additional content to the file
with open(file_name, "a") as file:
    file.write("Appending a new line to the file.\n")

print("Additional content appended successfully.")

# Step 4: Verify the updated file content
print("\nUpdated file content:")
with open(file_name, "r") as file:
    updated_content = file.read()

# Display the updated file content
print(updated_content)

