![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href = "https://www.paypal.com/donate/?hosted_button_id=5JK8CUWFUU9B6">![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)</a>

# Image Quotes Generator
<h3>This script creates high-quality image quotes, perfect for Instagram/Pinterest

**in less than 5 seconds per 100+ images!**</h3>

<h2 id="examples">📷 Examples</h2>

<img src="https://github.com/SamuraiPolix/ChristianPostMaker/assets/52662032/978d6835-c96b-4525-84a3-1d8c7cf9c2cf" width="45%">
<img src="https://github.com/SamuraiPolix/ChristianPostMaker/assets/52662032/cc4562a6-40ba-46ca-b139-9e5f5d69a937" width="45%">

## 📝 Table of Contents

1. [About](#about)
2. [How it works](#working)
3. [How To Run](#how_to)
4. [Available Topics](#topics)
5. [Built Using](#built_using)
6. [Final Results](#results)
7. [Note](#note)

<h2 id="about">🧐 About</h2>

This is one of my first Python projects, hope you get the most out of it :)

I used it to sell Fitness and Christian quotes on Fiverr for a while.


<h2 id="working">💭 How it works</h2>

<h4>#1 Content</h4>
After choosing the topics I wanted, I got a list of quotes and a stock of 50+ background images - both related to the picked topic.

<h4>#2 Prepping</h4>

After getting enough images, I run those 2 functions:

helper.cut_images_new(): to crop the images to the desired dimensions.

helper.darken_images(): to darken the images so the text looks better.

<h4>#3 Editing</h4>
The script works by taking a background image from '/sources/images/{topic}' and a quote from the .txt file, and combining them into 1 photo.

I am using **PILLOW** to generate the text in different fonts and combine it with the background image.

All the images are copyright-free from stock footage websites, and the fonts are copyright-free as well.

<h2 id="how_to">🏁 How to run</h2>

Follow the instructions given below to get this script up and running on your device.

1. Download this repository as zip file / using git.
2. Open the folder.
3. Make sure all the required modules are installed. (`pip install -r requirements.txt`)
4. Open main.py
5. set the number of posts you want, your logo, and choose a topic (It can be one of the available topics, or you can add another one, how to is explained here)
```python
TOPIC = "fitness"
SHOW_AUTHOR = True
CUSTOMER_NAME = "your_name"
NUM_OF_POSTS = 35
```
6. RUN!
7. And that's it! In about 5 seconds, you will have 100+ generated images!
8. You can find your images in the `generated/your_name/` directory.

<h2 id="topics">📋 Available Topics</h2>

1. Christian
2. Fitness

To create a new topic, please follow these steps:

1. Create a {topic}.txt file inside /sources/text_data
2. Run "helper.create_new_topic_dirs(TOPIC, project_dir)" to auto create all the directories needed
3. Add images to /sources/images/{topic}
4. Run "helper.cut_images_new(images_folder, images_folder_cropped)" to crop the images to 1080 X 1350
(you can change the dimension inside the function)
5. Run "helper.darken_images(images_folder_cropped, images_folder_cropped_darken)" if you want to make the images darker
(it makes the text look better)

ANS THAT'S IT! :)
Feel free to create a Pull Request if you want to help others as well!


<h2 id="built_using">⛏️ Built Using</h2>

[PILLOW](https://pypi.org/project/Pillow/) - For generating text images


<h2 id="results">📷 Final Results</h2>

After running the script you will get:
1. The edited images.

<img src="https://github.com/SamuraiPolix/ChristianPostMaker/assets/52662032/cdbf3b02-0ddb-474d-adbc-b3a722b4ad0f" width="45%">
<img src="https://github.com/SamuraiPolix/ChristianPostMaker/assets/52662032/76139b36-8306-4146-91b2-b3bfa67723c4" width="45%">


2. A spreadsheet containing the file names, quotes, and authors, to make it easier to find the image you want.

<h2 id="note">🗒️ Note</h2>

Note that this script is very basic as of now. If you want to contribute, you are free to do so and you may even fork and improve this repository.
