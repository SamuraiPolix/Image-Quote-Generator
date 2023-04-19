import os
import post_handler
import helper


project_dir = os.getcwd().replace("\\", "/")
# Available topics: christian, fitness
TOPIC = "christian"

# Define the paths and values to everything
# If number of posts if set to -1, it will so as many posts as in the data file
number_of_posts = 81
images_folder = f"{project_dir}/sources/images/{TOPIC}"
images_folder_cropped = f"{images_folder}/cropped"
images_folder_cropped_darken = f"{images_folder_cropped}/darken"
text_file = f"{project_dir}/sources/text_data/{TOPIC}.txt"
font_dir = "C:/Users/samla/AppData/Local/Microsoft/Windows/Fonts/MouldyCheeseRegular-WyMWG.ttf"
output_folder = f"{project_dir}/customers/{TOPIC}"
logo_file = f"{project_dir}/sources/logo.png"
customer_name = "everythingod"


if __name__ == "__main__":
    # helper.create_new_topic_dirs(TOPIC, project_dir)

    # helper.cut_images_new(images_folder, images_folder_cropped)
    # helper.darken_images(images_folder_cropped, images_folder_cropped_darken)

    # LOGO
    post_handler.create_posts(images_folder=images_folder_cropped_darken, text_file=text_file,
                         font_dir=font_dir, output_folder=output_folder,
                         logo_file=logo_file, customer_name=customer_name, number_of_posts=number_of_posts)

    # NO LOGO
    # post_handler.create_posts(images_folder=images_folder_cropped_darken, text_file=text_file,
    #                      font_dir=font_dir, output_folder=output_folder,
    #                      customer_name=customer_name, number_of_posts=number_of_posts)

