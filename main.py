import post_handler
import helper_images

# Define the paths and values to everything
number_of_posts = 2
images_folder = "C:/Bots/ChristianPostMaker/sources/images/cropped/darken"
text_file = "C:/Bots/ChristianPostMaker/sources/quotes.txt"
font_dir = "C:/Users/samla/AppData/Local/Microsoft/Windows/Fonts/MouldyCheeseRegular-WyMWG.ttf"
output_folder = "C:/Bots/ChristianPostMaker/customers"
logo_file = "C:/Bots/ChristianPostMaker/sources/logo.png"
customer_name = "test1"


if __name__ == "__main__":
    # helper_images.cut_images(images_folder, f"{images_folder}/cropped")
    # helper_images.darken_images(images_folder, f"{images_folder}/darken")
    post_handler.create_posts(images_folder=images_folder, text_file=text_file,
                         font_dir=font_dir, output_folder=output_folder,
                         logo_file=logo_file, customer_name=customer_name, number_of_posts=number_of_posts)
