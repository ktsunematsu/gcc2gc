import re
import pickle

# Load the response from the file
with open('response.pkl', 'rb') as f:
    response = pickle.load(f)

# Extract the OCR results
texts = response.text_annotations

# Define the patterns to search for
patterns = [
    "燃やす",
    "燃やさない",
    "資源",
    r"(?<!\d)([1-9]|1[0-2])月(?!\d)",
    r"\b([1-9]|[12][0-9]|3[01])\b",
]

# Search for the patterns in the OCR results
for text in texts:
    for pattern in patterns:
        if re.search(pattern, text.description):
            print(f'Page {page_index + 1}, Pattern "{pattern}" found: {text.description}')