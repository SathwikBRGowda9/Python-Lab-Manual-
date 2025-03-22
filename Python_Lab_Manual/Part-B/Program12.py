#4.	Demonstrate use of Dictionaries

# Demonstrating the use of Dictionaries in Python

# Create a dictionary to store student information
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "grades": [85, 90, 78]
}

# Access values in the dictionary
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Major:", student["major"])
print("Student Grades:", student["grades"])

# Add a new key-value pair to the dictionary
student["graduation_year"] = 2025
print("\nUpdated Dictionary:", student)

# Update an existing value in the dictionary
student["age"] = 21
print("\nDictionary after updating age:", student)

# Remove a key-value pair from the dictionary
student.pop("major")
print("\nDictionary after removing 'major':", student)

# Loop through the dictionary
print("\nIterating through the dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

