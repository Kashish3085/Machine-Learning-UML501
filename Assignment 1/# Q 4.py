# Q 4
import numpy as np 

# a.
from PIL import Image

def img_to_array(path):
    img = Image.open(path)
    img_array = np.array(img)
    if img.mode == 'RGB':
        np.savetxt("rgb_image.txt", img_array.reshape(-1, 3), fmt='%d')
    elif img.mode == 'L':
        np.savetxt("gray_image.txt", img_array, fmt='%d')
    else:
        raise ValueError("Unsupported image mode")
    print("Saved successfully!")
     
# b.
gray_loaded = np.loadtxt("gray_image.txt", dtype=int)
rgb_loaded = np.loadtxt("rgb_image.txt", dtype=int).reshape(-1, 3)