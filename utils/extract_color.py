import cv2
import numpy as np

# Read the image
img = cv2.imread('01_P1-1.png')

# Convert the image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color ranges for cyan, pink, and green
color_ranges = {
    'cyan': ([80, 100, 100], [100, 255, 255]),
    'pink': ([140, 80, 100], [170, 255, 255]),
    'green': ([35, 100, 100], [70, 255, 255])
}

for color, (lower, upper) in color_ranges.items():
    # Create a mask for the color
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)

    # Apply the mask to extract the color
    extracted = cv2.bitwise_and(img, img, mask=mask)

    # Save the extracted image
    cv2.imwrite(f'{color}_extracted.png', extracted)