import urllib.request

import cv2
import numpy as np
import winsound
import ColorObject as cod
import time

cap = cv2.VideoCapture(0)
url = 'http://192.168.0.100:8080/shot.jpg'

yellowDetector = cod.ColorObject('yelow', [20, 150, 150], [40, 255, 255])
orangeDetector = cod.ColorObject('Orng', [5, 150, 150], [15, 235, 250])
blueDetector = cod.ColorObject('Blue', [110, 50, 50], [120, 255, 255])
greenDetector = cod.ColorObject('Green', [45, 50, 50], [75, 255, 255])
redDetector = cod.ColorObject('Red', [120, 120, 140], [180, 250, 200])
whiteDetector = cod.ColorObject('White', [70, 0, 180], [180, 120, 255])


def getRubixImage():
    _, img = cap.read()
    # req = urllib.request.urlopen(url)
    # rcube_array = np.array(bytearray(req.read()), dtype=np.uint8)
    # img = cv2.imdecode(rcube_array, -1)
    return img  # cv2.resize(rcube, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)


start_time = time.time()
end_time = 0
while True:
    rcube = getRubixImage()
    no_of_contour = 0
    for detector in (whiteDetector, blueDetector, redDetector, greenDetector, yellowDetector, orangeDetector):
        contours = detector.getColorContours(rcube)
        no_of_contour = no_of_contour + len(contours)
        detector.detectAndDraw(rcube, contours)
        end_time = time.time()

    if no_of_contour == 9 and (end_time - start_time) > 10:
        winsound.Beep(2500, 1000)
        start_time = time.time()
        time.sleep(5)

    cv2.imshow('Rubix\'s Cube', rcube)

    # Exit condition
    if cv2.waitKey(5) & 0xFF == 27:
        break

# cap.release()
cv2.destroyAllWsindows()
