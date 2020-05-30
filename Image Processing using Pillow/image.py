from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')
filter_img = img.convert('L')
filter_img.save("pikachu_grey.png", 'png')
crooked = filter_img.rotate(180)
crooked.show()
