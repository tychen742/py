from PIL import Image

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))


# img = Image.open('/Users/tychen/PycharmProjects/thinkcspy_practicies/test.jpg')
img = Image.open('/Users/tychen/PycharmProjects/thinkcspy_practices/test.jpg')
# img = Image.open('test.jpg', 'jpg')
img1 = Image.open('test.jpg')
img2 = Image.open('pexels-photo-57690.jpeg')
img3 = Image.open('bass.gif')

print(img1)
print(img2)
print(img3)

img1.show()
# img2.show()
# img3.show()

img1.size()

with Image.open("bass.gif") as im:
    width, height = im.size
print(im.size())

# print(img1.getWidth())
# print(img.getHeight())

# imghdr.what('test.jpg')
