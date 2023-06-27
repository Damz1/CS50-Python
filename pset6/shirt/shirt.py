import sys
import os
from PIL import Image, ImageOps

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    sys.exit("Please provide exactly two command-line arguments.")

# Extract the input and output file names from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input and output file names end with .jpg, .jpeg, or .png (case-insensitive)
if not (input_file.lower().endswith(('.jpg', '.jpeg', '.png')) and
        output_file.lower().endswith(('.jpg', '.jpeg', '.png'))):
    sys.exit("Input and output file names must end with .jpg, .jpeg, or .png.")

# Check if the output file has the same extension as the input file
if os.path.splitext(input_file)[1] != os.path.splitext(output_file)[1]:
    sys.exit("The output file must have the same extension as the input file.")

# Check if the input file exists
if not os.path.isfile(input_file):
    sys.exit("The specified input file does not exist.")

# Open the input image
input_image = Image.open(input_file)

# Open the shirt image
shirt_image = Image.open("shirt.png")

# Resize and crop the input image to match the shirt image size
resized_input_image = ImageOps.fit(input_image, shirt_image.size)

# Overlay the shirt image on the resized input image
resized_input_image.paste(shirt_image, (0, 0), mask=shirt_image)

# Save the resulting image
resized_input_image.save(output_file)

print("Overlay complete.")
