from PIL import Image, ImageFilter
img = Image.open('./Pokedex/astro.jpg')
img.thumbnail((900, 565))
img.save("thumbnail.png",'png')
print(img.size)