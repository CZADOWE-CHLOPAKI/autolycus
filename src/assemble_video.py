import cv2
import numpy as np
import glob


def main():
    img_array = []
    for filename in glob.glob('images/dankmemes/*.*'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for i in range(len(img_array)):
        img_array[i] = cv2.resize(img_array[i], size, interpolation=cv2.INTER_AREA)

    for image in img_array:
        for _ in range(60):
            out.write(image)
    out.release()


if __name__ == "__main__":
    main()
