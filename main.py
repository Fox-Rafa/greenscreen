import PIL
from PIL import Image

print("write the name of the image with the greenscreen with the suffix(jpg)")
image = input()

print("write the image to put in the background with the suffix(jpg)")
back = input()

#opens the images
im = Image.open(image)
imm = Image.open(back)

#gets the size of the greenscreen image
x, y = im.size

#resizes the background image to fit into the greenscreen image
imm = imm.resize((x, y))

#loads them as pixels
img = im.load()
immg = imm.load()

#this
t=55

#runs through every pixel in the image
for i in range(x):
    for j in range(y):
        r, g, b = img[i, j]
        #if the value of the green pixel is at least 't' larger than the values of the red and blue pixel
        if g-r>t and g-b>t:
            #changes the value of the original image pixel to the ne image
            img[i, j]=immg[i, j]

#saves the image
im.save("output.jpg")

#displays the image
im.show()
