import base64

import cv2
import numpy as np


with open("mask.png", "rb") as img_file:
    encoded_data = base64.b64encode(img_file.read()).decode("utf-8")
    img_file.close()

with open("mask.py", "w") as py_file:
    py_file.write(f'image_data = """{encoded_data}"""\n')
    py_file.close()
