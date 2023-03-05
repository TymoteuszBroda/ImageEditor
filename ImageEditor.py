from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

os.mkdir(path)
os.mkdir(pathOut)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L') 

    factor = 1.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)

    clean_name = os.path.splitext(filename) [0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
