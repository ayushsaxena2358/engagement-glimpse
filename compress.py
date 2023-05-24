from PIL import Image
import os

# Define the path to the img folder
folder_path = "img/"

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Open the image file
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Compress the image by reducing the quality
        image.save(image_path, optimize=True, quality=70)

        # Close the image file
        image.close()

print("Image compression complete.")
