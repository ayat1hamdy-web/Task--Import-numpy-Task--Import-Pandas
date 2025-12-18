import numpy as np

# 1. Create Arrays
A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

# 2. Perform Operations
addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B

# 3. Apply NumPy Functions
mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)

# Dot product (sum of products of corresponding elements)
dot_product = np.dot(A, B)

# Reshape A into a 5x1 matrix
reshaped_A = A.reshape(5, 1)

# Displaying results
print("Array A:", A)
print("Array B:", B)
print("-" * 20)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("-" * 20)
print(f"Mean of A: {mean_A}, Max: {max_A}, Min: {min_A}")  
print("Dot Product:", dot_product)
print("Reshaped A (5x1):\n", reshaped_A)