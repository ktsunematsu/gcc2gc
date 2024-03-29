from google.cloud import vision
from pdf2image import convert_from_path
import os
import io  # Add this line
import json
import re
from PIL import Image
import pickle

# Create a client
client = vision.ImageAnnotatorClient()

# Convert the PDF to images
images = convert_from_path("01_P1.pdf")

for page_index, img in enumerate(images):
    # Convert the PIL Image to a byte array
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    # Create an Image object for Google Cloud Vision
    vision_image = vision.Image(content=img_byte_arr)

    # Perform text detection
    response = client.text_detection(
        image=vision_image, image_context={"language_hints": ["ja"]}
    )

    # Save the response to a file
    with open("response.pkl", "wb") as f:
        pickle.dump(response, f)
