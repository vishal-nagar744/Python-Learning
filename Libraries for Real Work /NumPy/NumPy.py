# NumPy Arrays
# Python list → NumPy array me convert:

import numpy as np

py_list = [1, 2, 3, 4, 5]

np_array = np.array(py_list)

print("Python List:", py_list)
print("NumPy Array:", np_array)




# Array Creation

# 1D array
arr1 = np.array([1,2,3])

# 2D array
arr2 = np.array([[1,2,3],[4,5,6]])

# Range array
arr3 = np.arange(1,11)  # 1 to 10 numbers

# Zeros & Ones
arr4 = np.zeros((2, 3))   # 2x3 matrix of zeros
arr5 = np.ones((3, 3))    # 3x3 matrix of ones


print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)



# Matrix Operations

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", mat1 + mat2)
print("Matrix Multiplication:\n", np.dot(mat1, mat2))
print("Transpose:\n", mat1.T)



# Real-Life NumPy Examples
# Stock Price Analysis

# Imagine karo tumhe ek company ke stock prices diye gaye hain aur tumhe average, highest, lowest nikalna hai.

import numpy as np

# Last 7 days stock prices
stock_prices = np.array([120, 125, 122, 130, 128, 127, 135])

print("Stock Price Analysis")
print("Average Price:", np.mean(stock_prices))
print("Highest Price:", np.max(stock_prices))
print("Lowest Price:", np.min(stock_prices))