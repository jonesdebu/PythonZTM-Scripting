import os
import sys
import glob
from PIL import Image

# grab cmd line args
grab_dir = None
save_dir = None
illegal_chars = {'#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', ' ', '$', '!', '\'', '\"', ':', '@', '+', '`',
                 '|', '='}
try:
    grab_dir = sys.argv[1]
    save_dir = sys.argv[2]
    print(f"Grab dir = {grab_dir} : Save dir = {save_dir}")

    for char in illegal_chars:
        if char in save_dir:
            print(f"Illegal character {char} found in save_dir name.... replacing with _ ....\n")
            # replace returns a new string object so have to set save_dir = to the statement
            save_dir = save_dir.replace(char, '_')
            print(f"New save dir name is {save_dir}\n")

except IndexError as e:
    print("You must enter the name of the jpeg dir with the photos you wish to convert and the name if the dir you wish"
          " to save the converted photos to as cmd line arguments.\n"
          "For Example: python jpeg_to_png_converter.py grab_dir save_dir\n")
    exit()


# check if new directory exists if not create
if os.path.isdir(save_dir):
    print(f"Directory {save_dir} exists in current directory\n")
else:
    os.mkdir(save_dir)

# loop through images in pokedex (or grab dir)
jpeg_files = glob.glob(grab_dir + '/*.jpg')
for jpeg in jpeg_files:
    # convert and save to new directory
    filename = jpeg.split('/')[1].split('.')[0]
    png_img = Image.open(jpeg).save(save_dir + '/' + filename + '.png', 'png')
