import os
import random
import re
import textwrap
import time
from string import ascii_letters

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

import helper
import json_handler


def create_dirs(output_folder, customer_name):
    # create a folder for this customer if it doesn't exist
    output_path = f"{output_folder}/{customer_name}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Create folder inside for images
    # if not os.path.exists(f"{output_path}/verse_images"):
    #     os.makedirs(f"{output_path}/verse_images")
    return output_path


def create_posts(images_folder, text_file, quote_font, author_font, output_folder, customer_name, number_of_posts, logo_file: str = None, show_author : bool = False):
    # json_data = json_handler.get_data(json_file)
    # verses: str = json_data[0]
    # refs: str = json_data[1]

    # Read the text file into a list of lines
    with open(text_file, 'r', encoding='utf-8') as file:
        quotes = file.readlines()

    # If number_of_posts is set to -1, it will do it for the amount of quotes there is in the data file
    if number_of_posts == -1:
        number_of_posts = len(quotes) - 1

    run_time_average = 0
    if number_of_posts > 1:
        start_time_total = time.time()

    # Get list of photos in the specified folder and shuffle it
    image_num = list()
    image_files = [f"{images_folder}/{file}" for file in os.listdir(images_folder) if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")]
    random_for_image = random.randint(0, len(image_files) - 1)
    for i in range(number_of_posts):
        image_num.append((random_for_image + i) % len(image_files))
    random.shuffle(image_num)

    # Data for spreadsheet
    spreadsheet_col1 = list()
    spreadsheet_col2 = list()
    spreadsheet_col3 = list()

    # Creating folder for customer
    output_path = create_dirs(output_folder, customer_name)

    for i in range(number_of_posts):
        start_time = time.time()
        print(f"Creating Post #{i}")

        author_text = ""
        quote_text = ""
        text = quotes[i]
        quote = text.split(":::")
        quote_text = quote[0]
        if show_author and quote_text != text:
            author_text = quote[1]
            if author_text.rstrip(" ") == "":
                author_text = None

        # Choose a random image file from the list
        random_image_num = image_num[0]
        del image_num[0]
        image_file = image_files[random_image_num]

        image_license = image_file.split('/')
        image_license = image_license[len(image_license)-1]
        image_license = image_license.split('-')
        image_license = image_license[len(image_license)-1].rstrip(".jpg")

        file_name = f"/{i}-{image_license}.jpg"
        create_post(image_file=image_file, quote_text=quote_text,
                         quote_font=quote_font, author_font=author_font, output_path=output_path, file_name=file_name,
                         logo_file=logo_file, customer_name=customer_name, author_text=author_text)

        # Add to spreadsheet
        spreadsheet_col1.append(file_name.strip("/"))
        spreadsheet_col2.append(author_text)
        spreadsheet_col3.append(quote_text)

        end_time = time.time()
        run_time = end_time - start_time
        run_time_average += run_time
        print(f"\033[0;34m DONE #{i}, Run time:", round(run_time, 2), "seconds! \033[0m", output_path)

    helper.add_sheets(file_names=spreadsheet_col1, output_path=output_path, customer_name=customer_name,
                      authors=spreadsheet_col2, quotes=spreadsheet_col3)

    if number_of_posts > 1:
        run_time_average /= number_of_posts
        end_time_total = time.time()
        run_time_total = end_time_total - start_time_total
        print(f"\n\033[0;32mDone making {number_of_posts} posts for {customer_name}!"
              f"\nTotal run time:", round(run_time_total, 2), "seconds = ", round(run_time_total / 60, 2), " minutes!",
              f"\nAverage run time:", round(run_time_average, 2), "seconds!\033[0m")


def create_post(image_file, quote_text, quote_font, author_font, output_path, file_name, logo_file, customer_name, author_text: str = None):
    # Open specific image
    img = Image.open(image_file)

    # Load selected font
    quote_font = ImageFont.truetype(font=f'{quote_font}', size=75)

    # Create DrawText object
    draw = ImageDraw.Draw(im=img)

    # Define our text:
    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    # avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    # max_char_count = int(img.size[0] / avg_char_width)
    max_char_count = 25
    # Create a wrapped text object using scaled character count
    new_text = textwrap.fill(text=quote_text, width=max_char_count)
    # FIX FONT WITH SPACES
    new_text = new_text.replace(" ", "  ")
    # new_text = helper_images.split_string(text, max_char_count)
    # Define the positions of logo and text
    x_logo = 0
    y_logo = 1100
    x_text = img.size[0] / 2
    y_text = img.size[1] / 2
    position = (x_text, y_text)

    # Draw the shadow text
    shadow_color = (0, 0, 0, 128)
    shadow_position = (x_text+5, y_text+5)
    draw.text(shadow_position, new_text, font=quote_font, fill=shadow_color, anchor='mm', align='center')

    # Add main text to the image
    draw.text(position, text=new_text, font=quote_font, fill=(255, 255, 255, 255), anchor='mm',
              align='center')

    if author_text is not None:
        # Add author text
        # Count '\n' in the text to see how many lines there are
        author_font = ImageFont.truetype(font=f'{author_font}', size=45)
        num_of_lines = new_text.count("\n") + 1
        line_height = 55     # TODO CHECK REAL HEIGHT
        text_height = line_height * num_of_lines + 40
        # TODO CHANGE AUTHORS FONT
        author_position = (position[0], position[1] + text_height)
        draw.text(author_position, text=author_text, font=author_font, fill=(255, 255, 255, 255), anchor='mm', align='center')

    if logo_file is not None:
        # Open logo file
        img_logo = Image.open(logo_file)

        # Reduce the alpha of the overlay image by 30%
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

        # file_name

        # Save the image
        img_with_logo_rgb.save(f"{output_path}/{file_name}")
        # combined.show()
        return f"{output_path}/{file_name}"

    # If logo was off
    # Save the image
    img.save(f"{output_path}/{file_name}")
    # combined.show()
    return f"{output_path}/{file_name}"

