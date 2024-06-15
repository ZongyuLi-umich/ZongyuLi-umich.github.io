from PIL import Image
import numpy as np
import os

imgarray1 = 196 * np.ones([600,600,3])
with Image.open('myaiphoto.png') as img:
    # Convert the image to a NumPy array
    img_array = np.array(img)
    imgarray1[200:400, 200:400, :] = img_array

image = Image.fromarray(imgarray1.astype(np.uint8))
image.save('myaiphoto_large.png')