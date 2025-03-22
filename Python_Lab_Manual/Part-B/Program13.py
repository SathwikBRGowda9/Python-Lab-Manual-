#. Demonstrate use of tuples in python

# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements of a tuple
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Checking the length of the tuple
print("\nNumber of fruits:", len(fruits))

# Using a tuple in a loop
print("\nList of fruits:")
for fruit in fruits:
    print(fruit)

# Attempting to modify a tuple (immutable nature)
try:
    fruits[0] = "orange"  # This will raise an error
except TypeError as e:
    print("\nTuples are immutable! Error:", e)

# Unpacking a tuple
print("\nUnpacking the tuple:")
fruit1, fruit2, fruit3 = fruits
print("Fruit 1:", fruit1)
print("Fruit 2:", fruit2)
print("Fruit 3:", fruit3)
