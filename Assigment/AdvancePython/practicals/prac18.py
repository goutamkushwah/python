# WAP for Numpy in python

# -------------------------------------
# WAP FOR NUMPY IN PYTHON
# -------------------------------------

import numpy as np

# 1️⃣ Creating NumPy Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)


# 2️⃣ Array Attributes
print("\nArray Shape:", arr2.shape)
print("Array Size:", arr2.size)
print("Array Data Type:", arr2.dtype)


# 3️⃣ Arithmetic Operations
print("\nAddition:", arr1 + 2)
print("Multiplication:", arr1 * 3)
print("Square:", arr1 ** 2)


# 4️⃣ Indexing and Slicing
print("\nFirst Element:", arr1[0])
print("Slice (1 to 3):", arr1[1:4])


# 5️⃣ Reshaping Array
reshaped = arr1.reshape(5, 1)
print("\nReshaped Array:\n", reshaped)


# 6️⃣ Statistical Functions
print("\nMean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))


# 7️⃣ Creating Special Arrays
zeros = np.zeros((2, 2))
ones = np.ones((2, 2))
identity = np.eye(3)

print("\nZeros Array:\n", zeros)
print("Ones Array:\n", ones)
print("Identity Matrix:\n", identity)