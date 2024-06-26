![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href = "https://www.paypal.com/donate/?hosted_button_id=5JK8CUWFUU9B6">![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)</a>

# Image Quotes Generator
<h3>This script creates high-quality image quotes, perfect for Instagram/Pinterest

**in less than 5 seconds per 100+ images!**</h3>

<h2 id="examples">📷 Examples</h2>

<img src="https://github.com/SamuraiPolix/ImageQuoteGenerator/assets/52662032/526f7676-829f-4b77-aedd-cba775a95ab5" width="85%">
<img src="https://github.com/SamuraiPolix/ImageQuoteGenerator/assets/52662032/1bfadae8-15ec-4b43-ad4d-209e24ddfbb6" width="85%">


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

<img src="https://github.com/SamuraiPolix/QuoteGenerator/assets/52662032/06119ee9-3b64-4a43-8305-5ff686187a41" width="45%">
<img src="https://github.com/SamuraiPolix/QuoteGenerator/assets/52662032/95eea51f-31e3-487b-981a-a89e3156dec7" width="45%">
<img src="https://github.com/SamuraiPolix/QuoteGenerator/assets/52662032/2a267ced-e5b6-4648-ba82-d1b693681bc8" width="45%">
<img src="https://github.com/SamuraiPolix/QuoteGenerator/assets/52662032/70b0f651-030c-4052-bdcf-a5814562f763" width="45%">

2. A spreadsheet containing the file names, quotes, and authors, to make it easier to find the image you want.


<h2 id="note">🗒️ Note</h2>

Note that this script is very basic as of now. If you want to contribute, you are free to do so and you may even fork and improve this repository.
