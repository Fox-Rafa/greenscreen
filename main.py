import PIL
from PIL import Image

image = 'Z.jpg'

img = Image.open(image)
img = img.load()
x, y=img.size()
t=55

for i in range(x):
    for j in range(Y):
        r, g, b = img[i, j]
        if g-r>t&&g-b>t:
            img[i, j]=(255, 0, 0)

img.show()
