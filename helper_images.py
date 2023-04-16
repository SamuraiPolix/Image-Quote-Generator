from PIL import Image, ImageEnhance
import os


def darken_images(images_folder, output_folder):
    # Set desired darkness
    dark = 0.5

    # Loop through all the images in the directory
    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image
            filepath = os.path.join(images_folder, filename)
            img = Image.open(filepath)

            # Create an enhancer object for the image
            enhancer = ImageEnhance.Brightness(img)

            # Reduce the brightness by a factor of 'dark'
            dark_img = enhancer.enhance(dark)

            # Save the cropped image
            dark_img.save(f"{output_folder}/{filename}")


def cut_images(images_folder, output_folder):
    # Set the target size
    target_size = (1080, 1350)

    # Loop through all the images in the directory
    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image
            filepath = os.path.join(images_folder, filename)
            img = Image.open(filepath)

            # Get the size of the image
            width, height = img.size

            # Calculate the coordinates for cropping
            left = (width - target_size[0]) // 2
            top = (height - target_size[1]) // 2
            right = left + target_size[0]
            bottom = top + target_size[1]

            # Crop the image
            img = img.crop((left, top, right, bottom))

            # Save the cropped image
            img.save(f"{output_folder}/{filename}")
