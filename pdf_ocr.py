from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
from pdf2image import convert_from_path
import numpy as np

# Convert the PDF to images
images = convert_from_path('01_P1.pdf')

for page_index, img in enumerate(images):
    # Convert the image to grayscale
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

    # Extract text from image using Tesseract
    result = pytesseract.image_to_data(gray, output_type=Output.DICT)

    # Draw the OCR result on the image
    for i in range(len(result['text'])):
        if int(result['conf'][i]) > 60:
            (x, y, w, h) = (result['left'][i], result['top'][i], result['width'][i], result['height'][i])
            gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the drawn image
    cv2.imwrite(f'output_{page_index}.png', gray)