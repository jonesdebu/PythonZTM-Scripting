from PIL import Image, ImageFilter
import os

img = Image.open('pokedex/bulbasaur.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
grey_scale_img = img.convert('L')
grey_scale_img = grey_scale_img.rotate(180)
grey_scale_img = grey_scale_img.resize((180, 180))

print(f"{img.format}, {img.size}, {img.mode}")

filtered_img.save("pokedex/blur.png", "png")
grey_scale_img.save("pokedex/grey.png", "png")

filtered_img.show()
grey_scale_img.show()

os.remove('pokedex/blur.png')
os.remove('pokedex/grey.png')




