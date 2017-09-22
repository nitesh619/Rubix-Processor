import urllib.request

import cv2
import numpy as np

import ColorObject as cod

# cap = cv2.VideoCapture(0)
url = 'http://192.168.0.100:8080/shot.jpg'


def getRubixImage():
    # _, rcube = cap.read()
    req = urllib.request.urlopen(url)
    rcube_array = np.array(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(rcube_array, -1)
    return cv2.resize(img, None, fx=.5, fy=.5, interpolation=cv2.INTER_CUBIC)


while True:
    rcube = getRubixImage()

    yellowDetector = cod.ColorObject('yelow', [20, 150, 150], [40, 255, 255])
    orangeDetector = cod.ColorObject('Orng', [10, 120, 130], [20, 255, 255])
    blueDetector = cod.ColorObject('Blue', [110, 50, 50], [120, 255, 255])
    greenDetector = cod.ColorObject('Green', [45, 50, 50], [75, 255, 255])
    redDetector = cod.ColorObject('Red', [0, 150, 70], [10, 255, 255])
    whiteDetector = cod.ColorObject('White', [0, 0, 150], [2, 50, 255])

    for detector in (blueDetector, redDetector, greenDetector, yellowDetector, orangeDetector, whiteDetector):
        detector.detectAndDraw(rcube)

    cv2.imshow('Rubix\'s Cube', rcube)

    # Exit condition
    if cv2.waitKey(5) & 0xFF == 27:
        break

# cap.release()
cv2.destroyAllWindows()
