# Q 2
import numpy as np

# a.
a = np.array([[1,-2,3],[-4,5,-6]])

## i)
ab = np.abs(a)
print("Absolute:", ab)

## ii)
print("Flattened Percentiles:", np.percentile(a.flatten(),[25, 50, 75]))
print("Column Percentiles:", np.percentile(a, [25, 50, 75], axis=0))
print("Row Percentiles:", np.percentile(a, [25, 50, 75], axis=1))

## iii)
print("Mean:", [np.mean(a.flatten()), np.mean(a, axis=0), np.mean(a, axis=1)])
print("Median:", [np.median(a.flatten()), np.median(a, axis=0), np.median(a, axis=1)])
print("Std Dev:", [np.std(a.flatten()), np.std(a, axis=0), np.std(a, axis=1)])

# b.
b = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
print("Floor:", np.floor(b))
print("Ceil:", np.ceil(b))
print("Trunc:", np.trunc(b))
print("Round:", np.round(b))