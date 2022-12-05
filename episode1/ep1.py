import numpy as np
from PIL import Image
import glob

image_list = []

for image in glob.glob("C:\\Users\\Milica\\PycharmProjects\\numpy\\episode1/*.jpg"):
    image = Image.open(image)
    data = np.array(image)

    data = ((data - data.min()) / (data.max()-data.min())) * 255
    res_img = Image.fromarray(data.astype(np.uint8))
    image_list.append(res_img)

for i in range(len(image_list)):
    img = image_list[i]
    name = "new"+str(i+1)+".jpg"
    img.save(name)