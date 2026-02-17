# Pure Python lists (slow for big data)
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

print(a+b)
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
    
    
# NumPy – clean & fast
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

c = a + b           # No loop!
print(c)            # → [11 22 33 44 55]

##############################################

import numpy as np

# Create array from a list
a = np.array([10, 20, 30, 40, 50])

print(a)              # [10 20 30 40 50]
print(type(a))        # <class 'numpy.ndarray'>


# 1. From list
scores = np.array([85, 92, 78, 95])

# 2. From range-like
b = np.arange(10)          # 0, 1, 2, ..., 9

# 3. Zeros and ones (very useful!)
zeros = np.zeros(5)        # [0. 0. 0. 0. 0.]
ones  = np.ones(4)         # [1. 1. 1. 1.]

# 4. Simple sequence with steps
c = np.arange(0, 20, 5)    # [ 0  5 10 15]


# like range()
x = np.arange(0, 10, 2)         # [0 2 4 6 8]

# better control – number of points
y = np.linspace(0, 1, 11)       # [0.  0.1 0.2 ... 1. ]


#############################################

zeros = np.zeros(6)             # 1D: [0. 0. 0. 0. 0. 0.]
zeros2d = np.zeros((3, 4))      # 3 rows × 4 columns

ones = np.ones((2, 5))          # 2 × 5 array of 1s

full = np.full((3, 3), 7)       # all elements = 7



###########################################

I = np.eye(4)                   # 4×4 identity matrix
D = np.diag([10, 20, 30])       # diagonal matrix



arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr.shape)      # (3, 3)   → (rows, columns)
print(arr.ndim)       # 2        → number of dimensions
print(arr.size)       # 9        → total number of elements
print(arr.dtype)      # int64 (or int32 depending on system)

#EX:
# 1
np.zeros(8)                # shape: ?   ndim: ?

# 2
np.full((4, 5), 99)        # shape: ?   ndim: ?

# 3
np.linspace(0, 5, 10)      # shape: ?   ndim: ?


##########################################

mat = np.array([[ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12]])

print(mat[0, 2])     # 3    → row 0, column 2
print(mat[2, 3])     # 12
print(mat[1, -1])    # 8     (last column of row 1)


a = np.arange(20)          # [ 0  1  2  ... 19]

print(a[2:8])              # [2 3 4 5 6 7]
print(a[5:])               # [ 5  6 ... 19]   (from index 5 to end)
print(a[:7])               # [0 1 2 3 4 5 6]  (from start to 6)
print(a[::2])              # [ 0  2  4  6 ... 18]  (every second element)
print(a[::-1])             # [19 18 ... 1  0]     (reverse the array)

print(mat)
# Rows 0 to 1 (inclusive), columns 1 to 3 (not including 3)
print(mat[0:2, 1:3])
# All rows, only columns 0 and 2
print(mat[:, [0, 2]])
# Last two rows, first three columns
print(mat[-2:, :3])


###################################
print("view")
b = mat[1:3, 1:4]    # this is a view, not a copy
b[0, 0] = 99

print(mat)           # original matrix is changed!

c = mat[1:3, 1:4].copy()
c[0, 0] = 777        # does NOT affect mat

print(mat)
print(c)




###################################


import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)       # [11 22 33 44]
print(a - b)       # [-9 -18 -27 -36]
print(a * b)       # [ 10  40  90 160]
print(a / b)       # [0.1 0.1 0.1 0.1]
print(a ** 2)      # [ 1  4  9 16]
print(a % 3)       # [1 2 0 1]


print(a + 100)     # [101 102 103 104]
print(a * 5)       # [ 5 10 15 20]
print(a > 2)       # [False False  True  True]


###########################################
# Example 1: scalar + array
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a + 10)
# [[11 12 13]
#  [14 15 16]]

# Example 2: row vector + matrix
row = np.array([100, 200, 300])
print(a + row)
# [[101 202 303]
#  [104 205 306]]

# Example 3: column vector
col = np.array([[1000],
                [2000]])
print(a + col)
# [[1001 1002 1003]
#  [2004 2005 2006]]


import numpy as np

# مصروف 3 أيام (صفوف) × 4 أنواع (أعمدة)
# أكل ، قهوة ، مواصلات ، ترفيه
X = np.array([
    [50, 10, 20, 20],
    [80, 20, 30, 10],
    [40, 10, 20, 30]
])

print("البيانات الأصلية:")
print(X)


row_means = X.mean(axis=1, keepdims=True)

print("\nمتوسط كل يوم:")
print(row_means)


X_centered = X - row_means

print("\nالصرف بالنسبة لمتوسط اليوم:")
print(X_centered)

#######################################################




import numpy as np

data = np.array([23, 45, 12, 67, 89, 34, 56, 78, 91, 10])

print(data.sum())          # total = 505
print(data.mean())         # average ≈ 50.5
print(np.median(data))       # 50.5
print(data.std())          # standard deviation    الانحراف المعياري
print(data.var())          # variance                  التباين
print(data.min())          # 10   
print(data.max())          # 91
print(data.argmin())       # index of minimum → 9   Returns the index of the smallest value.
print(data.argmax())       # index of maximum → 8   Returns the index of the largest value.






# 2D example
scores = np.array([
    [85, 92, 78, 88],    # student 1
    [64, 70, 82, 91],    # student 2
    [95, 88, 76, 93]     # student 3
])

print(scores)

# axis=0 → along columns (per subject)
print("Mean per subject:", scores.mean(axis=0))
# [81.333 83.333 78.666 90.666]

# axis=1 → along rows (per student)
print("Mean per student:", scores.mean(axis=1))
# [85.75  76.75  88.  ]

print("Total per student:", scores.sum(axis=1))
print("Best score in each subject:", scores.max(axis=0))



# Normalize to [0,1]
normalized = (data - data.min()) / (data.max() - data.min())

print("N",normalized)

# Standardize (z-score)
z_scores = (data - data.mean()) / data.std()
print("S",z_scores)



############################################################
import numpy as np

a = np.arange(12)          # [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a.reshape(2, -1))    # -1 يعني "احسبها أنت"
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]

print(a.reshape(3, 2, 2))
# 3 blocks, each 2×2





mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(mat.T)
# or mat.transpose()
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]




print(mat.flatten())      # always returns a copy
# [1 2 3 4 5 6 7 8 9]

print(mat.ravel())        # usually returns a view (faster)
# [1 2 3 4 5 6 7 8 9]

print(mat.reshape(-1))    # another common way


########################################################

import numpy as np

scores = np.array([85, 92, 67, 45, 98, 73, 88, 55])

# Create a boolean mask
mask = scores >= 80
print(mask)
# [ True  True False False  True False  True False]

# Use the mask to filter
print(scores[mask])
# [85 92 98 88]

# One-liner (very common pattern)
print(scores[scores >= 80])
# [85 92 98 88]



# Replace low scores with 50
scores[scores < 60] = 50
print(scores)
# [85 92 67 50 98 73 88 50]


#Fancy
arr = np.arange(20) * 10
# [  0  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180 190]

# Select specific positions
indices = [2, 5, 8, 11]
print(arr[indices])
# [ 20  50  80 110]

# Can also use in 2D
mat = np.arange(20).reshape(4, 5)
print(mat)

rows = [0, 2, 3]
cols = [1, 3, 4]
print(mat[rows, cols])
# [ 1 13 19 ]

################################################

import numpy as np

# Single number
np.random.rand()        # e.g., 0.374

# 1D array of 5 numbers
np.random.rand(5)       # e.g., [0.56, 0.23, 0.89, 0.12, 0.44]

# 2D array 3x4
np.random.rand(3,4)     


print(np.random.randn(3, 4))



# رقم صحيح بين 0 و 9
print(np.random.randint(0, 10))

# مصفوفة 1D من 5 أرقام صحيحة
print(np.random.randint(0, 100, 5))

# مصفوفة 2D (3 صفوف × 4 أعمدة)
print(np.random.randint(10, 50, (3, 4)))


#############################################
import numpy as np

arr = [10, 20, 30, 40, 50]

x = np.random.choice(arr)
print(x)


x = np.random.choice(arr, size=3, replace=False)
print(x)


x = np.random.choice(arr, size=3, replace=True)
print(x)
