import os
import post_handler
import helper

# Available topics: christian, fitness
TOPIC = "christian"
SHOW_AUTHOR = False
CUSTOMER_NAME = "your_name"
# Disable limit: -1, it will create images according to the amount of quotes in the .txt file
NUM_OF_POSTS = -1

''' To create a new topic, please follow these steps:
1. Create a {topic}.txt file inside /sources/text_data
2. Run "helper.create_new_topic_dirs(TOPIC, project_dir)" to auto create all the directories needed
3. Add images to /sources/images/{topic}
4. Run "helper.cut_images_new(images_folder, images_folder_cropped)" to crop the images to 1080 X 1350
(you can change the dimension inside the function)
5. Run "helper.darken_images(images_folder_cropped, images_folder_cropped_darken)" if you want to make the images darker
(it makes the text look better)
ANS THAT'S IT! :)
Feel free to create a Pull Request if you want to help others as well!
'''

# Define the paths and values to everything
project_dir = os.getcwd().replace("\\", "/")
images_folder = f"{project_dir}/sources/images/{TOPIC}"
images_folder_cropped = f"{images_folder}/cropped"
images_folder_cropped_darken = f"{images_folder_cropped}/darken"
text_file = f"{project_dir}/sources/text_data/{TOPIC}.txt"
quote_font = f"{project_dir}/sources/fonts/MouldyCheeseRegular-WyMWG.ttf"       # Bible
# quote_font = f"{project_dir}/sources/fonts/Bebas-KM7y.ttf"       # Fitness
author_font = f"{project_dir}/sources/fonts/MangabeyRegular-rgqVO.otf"
output_folder = f"{project_dir}/generated/{TOPIC}"
logo_file = f"{project_dir}/sources/logo.png"


if __name__ == "__main__":
    # helper.create_new_topic_dirs(TOPIC, project_dir)

    # helper.fix_text_syntax(quote_font, text_file)

    # helper.cut_images_new(images_folder, images_folder_cropped)
    # helper.darken_images(images_folder_cropped, images_folder_cropped_darken)

    # LOGO
    post_handler.create_posts(images_folder=images_folder_cropped_darken, text_file=text_file,
                         quote_font=quote_font, author_font=author_font, output_folder=output_folder,
                         logo_file=logo_file, customer_name=CUSTOMER_NAME, number_of_posts=NUM_OF_POSTS, show_author=SHOW_AUTHOR)

    # NO LOGO
    # post_handler.create_posts(images_folder=images_folder_cropped_darken, text_file=text_file,
    #                      quote_font=quote_font, author_font=author_font, output_folder=output_folder,
    #                      customer_name=CUSTOMER_NAME, number_of_posts=NUM_OF_POSTS, show_author=SHOW_AUTHOR)

