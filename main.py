import os
from PIL import Image

path = 'opt/icons'
try:
    os.makedirs(path)
except FileExistsError:
    pass

for folder, sub_folder, file in os.walk(f'{os.getcwd()}\\images'):
    for f in file:
        image = Image.open(f"{folder}\\{f}")
        new_image = image.resize((128, 128)).rotate(-90)
        new_image.save(f"{os.getcwd()}//{path}//{f}","JPEG")
