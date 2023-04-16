import os
import random
import textwrap
import time
from string import ascii_letters

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

import json_handler


def create_dirs(output_folder, customer_name):
    # create a folder for this customer if it doesn't exist
    output_path = f"{output_folder}/{customer_name}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Create folder inside for images
    if not os.path.exists(f"{output_path}/verse_images"):
        os.makedirs(f"{output_path}/verse_images")
    return output_path


def create_posts(images_folder, text_file, font_dir, output_folder, customer_name, number_of_posts, logo_file: str = None):
    run_time_average = 0
    if number_of_posts > 1:
        start_time_total = time.time()

    # json_data = json_handler.get_data(json_file)
    # verses: str = json_data[0]
    # refs: str = json_data[1]

    quotes = ["test1", "test2"]


    # Get list of photos in the specified folder and shuffle it
    image_num = list()
    image_files = [f"{images_folder}/{file}" for file in os.listdir(images_folder) if file.endswith(".jpg") or file.endswith(".png")]
    random_for_image = random.randint(0, len(image_files) - 1)
    for i in range(number_of_posts):
        image_num.append((random_for_image + i) % len(image_files))
    random.shuffle(image_num)

    # Creating folder for customer
    output_path = create_dirs(output_folder, customer_name)

    for i in range(number_of_posts):
        start_time = time.time()
        print(f"Creating Post #{i}")

        text = quotes[i]

        # Choose a random image file from the list
        random_image_num = image_num[0]
        del image_num[0]
        image_file = image_files[random_image_num]
        file_name = f"/{i}-{random_image_num}.jpg"
        create_post(image_file=image_file, text=text,
                         font_dir=font_dir, output_path=output_path, file_name=file_name,
                         logo_file=logo_file, customer_name=customer_name)

        end_time = time.time()
        run_time = end_time - start_time
        run_time_average += run_time
        print(f"\033[0;34m DONE #{i}, Run time:", round(run_time, 2), "seconds! \033[0m", output_path)

    if number_of_posts > 1:
        run_time_average /= number_of_posts
        end_time_total = time.time()
        run_time_total = end_time_total - start_time_total
        print(f"\n\033[0;32mDone making {number_of_posts} posts for {customer_name}!"
              f"\nTotal run time:", round(run_time_total, 2), "seconds!"
                                                              f"\nAverage run time:", round(run_time_average, 2),
              "seconds = ", round(run_time_average / 60, 2), " minutes! \033[0m")


def create_post(image_file, text, font_dir, output_path, file_name, logo_file, customer_name):
    # Open specific image
    img = Image.open(image_file)

    # Load selected font
    font = ImageFont.truetype(font=f'{font_dir}', size=75)

    # Create DrawText object
    draw = ImageDraw.Draw(im=img)

    # Define our text:
    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    max_char_count = int(img.size[0] * .718 / avg_char_width)

    # Create a wrapped text object using scaled character count
    new_text = textwrap.fill(text=text, width=max_char_count)

    # Define the positions of logo and text
    x_logo = 0
    y_logo = 1100
    x_text = img.size[0] / 2
    y_text = img.size[1] / 2
    position = (x_text, y_text)

    # Draw the shadow text
    shadow_color = (0, 0, 0, 128)
    shadow_position = (x_text+5, y_text+5)
    draw.text(shadow_position, text, font=font, fill=shadow_color, anchor='mm')

    # Add main text to the image
    draw.text(position, text=new_text, font=font, fill=(255, 255, 255, 255), anchor='mm',
              align='center')

    if logo_file is not None:
        # Open logo file
        img_logo = Image.open(logo_file)

        # Reduce the alpha of the overlay image by 50%
        alpha = 0.5
        enhancer = ImageEnhance.Brightness(img_logo)
        img_logo_darken = enhancer.enhance(alpha)

        # Create a new image object with the same size as the background image
        img_with_logo = Image.new('RGBA', img.size, (0, 0, 0, 0))

        # Draw the background image onto the new image
        img_with_logo.paste(img, (0, 0))

        # Draw the overlay image onto the new image
        img_with_logo.paste(img_logo_darken, (int(x_logo), int(y_logo)), mask=img_logo_darken)

        # Convert from RGBA to RGB
        img_with_logo_rgb = img_with_logo.convert("RGB")

        # Save the image
        img_with_logo_rgb.save(f"{output_path}/{file_name}")
        # combined.show()
        return f"{output_path}/{file_name}"

    # If logo was off
    # Save the image
    img.save(f"{output_path}/{file_name}")
    # combined.show()
    return f"{output_path}/{file_name}"