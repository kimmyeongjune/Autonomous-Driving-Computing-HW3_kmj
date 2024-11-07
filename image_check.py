import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import patches

import files_management

img_left = files_management.read_left_image()
img_right = files_management.read_right_image()

_, image_cells = plt.subplots(1, 2, figsize=(20, 20))
image_cells[0].imshow(img_left)
image_cells[0].set_title('left image')
image_cells[1].imshow(img_right)
image_cells[1].set_title('right image')
plt.show()