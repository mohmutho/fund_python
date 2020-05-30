from PIL import Image, ImageFilter
img = Image.open('./Pokedex/Visitasi-Re-Akreditasi.jpg')
filter_img = img.resize((900, 565))
filter_img.save("visitasi.png",'png')
box = (100,100,400,400)
region = filter_img.crop(box)
region.save("visitasi_crop.png", 'png')
region.show()