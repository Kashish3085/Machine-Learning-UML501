# Q 3
import numpy as np

# a.
ar = np.array([10, 52, 62, 16, 16, 54, 453])
## i)
print("Sorted:", np.sort(ar))

## ii)
print("Sorted Indices:", np.argsort(ar))

## iii)
print("4 Smallest:", np.sort(ar)[:4])

## iv)
print("5 Largest:", np.sort(ar)[-5:])

# b.
arrr = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
## i)
print("Integers only:", arrr[arrr == arrr.astype(int)])

## ii)
print("Floats only:", arrr[arrr != arrr.astype(int)])