import cv2
import numpy as np
from scipy import stats

# Read the image
img = cv2.imread('crop_01_P1-1.png')

# Convert the image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate the mean of the HSV values
hsv_mean = np.mean(hsv, axis=(0, 1))

# Calculate the mode of the HSV values
hsv_mode = stats.mode(hsv.reshape(-1, hsv.shape[-1]), axis=0)[0]

# Print the mean and mode HSV values
print(f"Mean HSV: {hsv_mean}")
print(f"Mode HSV: {hsv_mode[0]}")