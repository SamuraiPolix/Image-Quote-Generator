import csv

from PIL import Image, ImageEnhance
import os


def split_string(string, max_chars_per_line):
    words = string.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) > max_chars_per_line:
            lines.append(current_line.strip())
            current_line = ""
        current_line += " " + word
    if current_line:
        lines.append(current_line.strip())

    # Re-combine lines to achieve even distribution of words
    num_lines = len(lines)
    if num_lines > 1:
        total_words = len(words)
        ideal_words_per_line = (total_words + num_lines - 1) // num_lines
        excess_words = total_words - ideal_words_per_line * (num_lines - 1)

        even_lines = []
        i = 0
        while i < num_lines - 1:
            line_words = words[:ideal_words_per_line]
            if excess_words > 0:
                line_words.append(words[ideal_words_per_line])
                excess_words -= 1
                words.pop(ideal_words_per_line)
            even_lines.append(" ".join(line_words))
            words = words[ideal_words_per_line:]
            i += 1
        even_lines.append(" ".join(words))
        return "\n".join(even_lines)
    else:
        return lines[0]


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


def cut_images_old(images_folder, output_folder):
    # Set the target size
    target_size = (1080, 1350)
    # Loop through all the images in the directory
    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image
            filepath = os.path.join(images_folder, filename)
            img = Image.open(filepath)
            resize_ration = min(target_size[0] / img.width, target_size[1] / img.height)

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


def cut_images(images_folder, output_folder):
    # Set desired ratio
    desired_ratio = 1080 / 1350

    # Loop through all files in input folder
    for filename in os.listdir(images_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Open the image
            img = Image.open(os.path.join(images_folder, filename))

            # Get image dimensions
            width, height = img.size
            ratio = width / height

            # Calculate new dimensions
            if ratio > desired_ratio:
                # Image is wider than desired ratio, crop width
                new_width = round(height * desired_ratio)
                new_height = height
            else:
                # Image is taller than desired ratio, crop height
                new_width = width
                new_height = round(width / desired_ratio)

            # Crop the image in the center
            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = left + new_width
            bottom = top + new_height
            img = img.crop((left, top, right, bottom))

            # Resize the image if necessary
            if img.size != (1080, 1350):
                img = img.resize((1080, 1350))

            # Save the image to output folder
            img.save(os.path.join(output_folder, filename))


def create_new_topic_dirs(topic, project_dir):
    # /customers/___
    if not os.path.exists(f"{project_dir}/customers/{topic}"):
        os.makedirs(f"{project_dir}/customers/{topic}")
    # /sources/images/___
    if not os.path.exists(f"{project_dir}/sources/images/{topic}"):
        os.makedirs(f"{project_dir}/sources/images/{topic}")
        os.makedirs(f"{project_dir}/sources/images/{topic}/cropped")
        os.makedirs(f"{project_dir}/sources/images/{topic}/cropped/darken")


def fix_text_syntax(font: str, text_file):
    with open(text_file, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    # Bebas can't display ’ -> replace with '
    if font.__contains__("Bebas"):
        # open file in read mode
        file = open(text_file, "r")
        replaced_content = ""

        # looping through the file
        for line in file:
            # stripping line break
            line = line.strip()

            # replacing the texts
            new_line = line.replace("’", "'").replace("’", "'")

            # concatenate the new string and add an end-line break
            replaced_content = replaced_content + new_line + "\n"

        # close the file
        file.close()

        # Open file in write mode
        write_file = open(text_file, "w")

        # overwriting the old file contents with the new/replaced content
        write_file.write(replaced_content)

        # close the file
        write_file.close()

def add_sheets(file_names: str, output_path: str, customer_name: str, authors: str, quotes: str):
    with open(f'{output_path}/{customer_name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Reference", "Verse"])
        for i in range(len(file_names)):
            writer.writerow([file_names[i], authors[i], quotes[i]])

