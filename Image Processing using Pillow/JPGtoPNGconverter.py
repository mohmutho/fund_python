import sys
import os
from PIL import Image
# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check is new\ exist, if not create it
if not os.path.exists(output_folder) :
    os.makedirs(output_folder)
# loop through pokedex
for filename in os.listdir(image_folder) :
    img = Image.open(f'{image_folder}{filename}')
    #untuk menghapuskan '.jpg' dengan diambil tupple ke 0
    clean_name = os.path.splitext(filename)[0]
    #convert to png
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
# convert images to png
# save them into new folder.
