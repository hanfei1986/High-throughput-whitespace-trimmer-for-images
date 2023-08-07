from PIL import Image
import glob

def trim(image_path):
    image = Image.open(image_path)
    border_color = image.getpixel((0, 0))

    left = 0
    right = image.width
    top = 0
    bottom = image.height

    for i in range(image.width):
        same_color = all([image.getpixel((i, j)) == border_color for j in range(image.height)])
        if not same_color:
            left = i-1
            break
    for i in range(image.width-1,-1,-1):
        same_color = all([image.getpixel((i, j)) == border_color for j in range(image.height)])
        if not same_color:
            right = i+1
            break
    for i in range(image.height):
        same_color = all([image.getpixel((j, i)) == border_color for j in range(image.width)])
        if not same_color:
            top = i-1
            break 
    for i in range(image.height-1,-1,-1):
        same_color = all([image.getpixel((j, i)) == border_color for j in range(image.width)])
        if not same_color:
            bottom = i+1
            break

    image = image.crop((left, top, right, bottom))
    return image

path = 'C:/Users/fhan/Desktop/Pictures/Raw\*.*'
for file in glob.glob(path):
    filename = file.split('\\')[-1]
    image = trim(file)
    image.save('C:/Users/fhan/Desktop/Pictures/Trimmed/'+filename)