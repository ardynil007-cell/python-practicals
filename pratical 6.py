# Q1. Create and access 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("First row:", matrix[0])
print("Element at row 2, column 3:", matrix[1][2])

# Q2. Row-wise and column-wise traversal

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Row-wise:")
for row in matrix:
    print(*row)
print("Column-wise:")
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col], end=" ")
    print()

# Q3. Sum of each row and column

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i, row in enumerate(matrix):
    print("Row", i + 1, "sum:", sum(row))
for col in range(len(matrix[0])):
    print("Column", col + 1, "sum:", sum(matrix[row][col] for row in range(len(matrix))))

# Q4. Matrix addition

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
for row in result: print(row)

# Q5. Transpose matrix

matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [list(row) for row in zip(*matrix)]
print("Original:", matrix)
print("Transpose:", transpose)

# Q6. NumPy array creation

a = np.array([1, 2, 3])
z = np.zeros((2, 3))
o = np.ones((2, 2))
for arr in (a, z, o):
    print(arr)
    print("Shape:", arr.shape, "Data type:", arr.dtype)

# Q7. NumPy indexing and slicing

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element:", a[1, 2])
print("Row:", a[0, :])
print("Column:", a[:, 1])
print("Slice:", a[:2, 1:])

# Q8. NumPy arithmetic

import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Q9. Statistical operations

import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Standard deviation:", np.std(a))

# Q10. Reshape array

import numpy as np
a = np.arange(1, 13)
print(a.reshape(3, 4))

# Q11. Matrix operations

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Addition:\n", A + B)
print("Matrix product:\n", A @ B)
print("Transpose:\n", A.T)

# Q12. Dataset analysis

import numpy as np
data = np.array([23, 25, 21, 28, 26, 24])
print("Values:", data)
print("Average:", data.mean())
print("Highest:", data.max())
print("Lowest:", data.min())
print("Above average:", data[data > data.mean()])

