import whatimage
import pyheif
from PIL import Image
import os

def decodeImage(bytesIo, index):
    with open(bytesIo, 'rb') as f:
        data = f.read()
        fmt = whatimage.identify_image(data)
    if fmt in ['heic', 'avif']:
        i = pyheif.read_heif(data)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        pi.save("new" + str(index) + ".jpg", format="jpeg")

# For my use I had my python file inside the same folder as the heic files
source = "./"

for index,file in enumerate(os.listdir(source)):
    decodeImage(file, index)