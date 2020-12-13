import sys
import math
import numpy as np
import cv2 as cv

from yoro import api


def draw_degree(image, degree):

    # Draw arrow
    length = min(image.shape[:2]) * 3 / 8
    rad = math.radians(degree + 90)

    ctr = np.intp((image.shape[1] / 2, image.shape[0] / 2))
    vec = np.intp((length * math.cos(rad), -length * math.sin(rad)))
    cv.arrowedLine(image, tuple(ctr), tuple(np.add(ctr, vec)),
                   (0, 85, 255), 2, cv.LINE_AA)


if __name__ == '__main__':

    # Parse arguments
    if len(sys.argv) < 3:
        print('Usage: %s <model_path> <test_image> [device]' % sys.argv[0])
        exit(-1)

    devType = api.DeviceType.Auto
    if len(sys.argv) > 3:
        if sys.argv[3] == 'cpu':
            devType = api.DeviceType.CPU
        elif sys.argv[3] == 'cuda':
            devType = api.DeviceType.CUDA

    # Import model and load image
    detector = api.RotationDetector(sys.argv[1], devType)
    image = cv.imread(sys.argv[2], cv.IMREAD_COLOR)

    # Run detector
    degree = detector.detect(image)

    # Show result
    print('Detection:', degree)
    draw_degree(image, degree)

    cv.imshow('Detection Result', image)
    cv.waitKey(0)
