# Q 1
# #Assignment 1
import numpy as np

# a.
arr1 = np.array([1,2,3,6,4,5])
rev = np.flip(arr1)
print("reversed array:",rev)

# b.
arr2 = np.array([[1,2,3],[2,4,5],[1,2,3]])
fl = arr2.flatten()
rv = arr2.ravel()
print("Flatten array using method 1:",fl)
print("Flatten array using method 2:",rv)

# c.
arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[1,2],[3,4]])
print("Are both arrays equal?",np.array_equal(arr3,arr4))

# d.
## i)
arr5 = np.array([1,2,3,4,5,1,2,1,1,1])
u, c = np.unique(arr5, return_counts=True)
freq = u[np.argmax(c)]
i = np.where(arr5==freq)[0]
print("Most frequent:", freq, "Indices:", i)

## ii)
arr6 = np.array([1,1,1,2,3,4,2,4,3,3])
u, c = np.unique(arr5, return_counts=True)
freq = u[np.argmax(c)]
i = np.where(arr6==freq)[0]
print("Most frequent:", freq, "Indices:", i)

# e.
m = np.matrix('[4,1,9;12,3,1;4,5,6]')
print("Sum:", m.sum())
print("Row-wise um:", m.sum(axis=1))
print("Column-wise sum:", m.sum(axis=0))

# f.
arr = np.array([[55,25,15],[30,44,2],[11,45,77]])
## i)
print("Sum of diagonals:", np.trace(arr))

## ii)
ev, evec = np.linalg.eig(arr)
print("Eigen Values:",ev)

## iii)
print("Eigen Vectors:",evec)

## iv)
inv = np.linalg.inv(arr)
print("Inverse:",inv)

## iv)
d = np.linalg.det(arr)
print("Determinant:",d)

# g.
## i)
p1 = np.array([[1,2],[2,3]])
q1 = np.array([[4,5],[6,7]])
prod = np.dot(p1,q1)
print("Multiplication:", prod)
print("Covariance:",np.cov(p1.T,q1.T))

## ii)
p2 = np.array([[1,2],[2,3],[4,5]])
q2 = np.array([[4,5,1],[6,7,2]])
prod = np.dot(p2,q2)
p = p2.flatten()
q = q2.flatten()
print("Multiplication:", prod)
print("Covariance:",np.cov(p.T,q.T))

# h.
x = np.array([[2,3,4],[3,2,9]])
y = np.array([[1,5,0],[5,10,3]])
inn = np.inner(x,y)
out = np.outer(x,y)
print("Inner:",inn)
print("Outer:",out)

from itertools import product
c = np.array(list(product(x.flatten(), y.flatten())))
print("Cartesian:",c)