import os
import numpy as np
import cv2

letter = ""
dir_path = os.path.join(r'E:\backUp\Dissertation\DataSet\images', letter)

len = len(os.listdir(dir_path))
index = 1


def sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


for file in get_files(dir_path):
    img = cv2.imread(os.path.join(dir_path, file))
    img = sharpen(img)
    img = img[:, ::-1, :]
    name = letter + str(len + index) + ".png"
    cv2.imwrite(os.path.join(dir_path, name), img)
    index += 1
