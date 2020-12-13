import sys
import math
import numpy as np
import cv2 as cv

from yoro import api


def draw_rbox(image, rbox):

    # Draw rotated bounding box
    boxPts = np.intp(
        cv.boxPoints(((rbox.x, rbox.y), (rbox.w, rbox.h), -rbox.degree)))
    cv.drawContours(image, [boxPts], 0, (0, 128, 0), 2, cv.LINE_AA)

    # Draw arrow
    length = rbox.h * 3 / 8
    rad = math.radians(rbox.degree + 90)

    ctr = np.intp((rbox.x, rbox.y))
    vec = np.intp((length * math.cos(rad), -length * math.sin(rad)))
    cv.arrowedLine(image, tuple(ctr), tuple(np.add(ctr, vec)),
                   (192, 0, 0), 2, cv.LINE_AA, 0, 0.2)

    # Draw label
    shift = rbox.h / 4
    vec = np.intp((shift * math.cos(rad), -shift * math.sin(rad)))
    cv.putText(image, str(rbox.label), tuple(np.subtract(ctr, vec)),
               cv.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 0), 2, cv.LINE_AA)


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
    detector = api.YORODetector(sys.argv[1], devType)
    image = cv.imread(sys.argv[2], cv.IMREAD_COLOR)

    # Run detector
    pred = detector.detect(image, 0.9, 0.7)

    # Show result
    for inst in pred:
        print(inst)
        draw_rbox(image, inst)

    cv.imshow('Detection Result', image)
    cv.waitKey(0)
