#Crop image and save
from PIL import Image
img = Image.open('image for croped/test.jpg')
img = img.resize((1280, 842), Image.ANTIALIAS)
img.save('final/croped.jpg')
img.show()

g
