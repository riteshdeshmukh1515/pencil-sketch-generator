import cv2 as cv
from pathlib import Path
from tkinter import Tk, filedialog

# Hide the root Tk window
Tk().withdraw()

# Ask user to select an image file
image_path = filedialog.askopenfilename(
    title="Select an image to convert to sketch",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")]
)

if not image_path:
    print("❌ No image selected. Exiting.")
    exit()

image_path = Path(image_path)

# Read the image
image = cv.imread(str(image_path))
if image is None:
    raise ValueError("❌ OpenCV could not read the image file. Make sure it is a valid image.")

# Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Invert grayscale image
inverted = cv.bitwise_not(gray)

# Apply Gaussian blur
blurred = cv.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blur = cv.bitwise_not(blurred)

# Create pencil sketch
sketch = cv.divide(gray, inverted_blur, scale=256.0)

# Save the result
output_path = image_path.with_stem(image_path.stem + "_sketch").with_suffix(".png")
cv.imwrite(str(output_path), sketch)

print(f"✅ Sketch saved as: {output_path.resolve()}")
