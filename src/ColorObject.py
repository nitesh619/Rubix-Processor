import cv2
import numpy as np


class ColorObject(object):
    kernel = np.ones((5, 5), np.uint8)

    def __init__(self, color, color_lower, color_upper):
        self.color = color
        self.color_lower = np.array(color_lower, np.uint8)
        self.color_upper = np.array(color_upper, np.uint8)

    def getColorMask(self, image_hsv):
        mask = cv2.inRange(image_hsv, self.color_lower, self.color_upper)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, ColorObject.kernel, iterations=1)
        return opening

    def getColorContours(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = self.getColorMask(hsv)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        return self.filterContors(contours)

    def detectShape(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # if the shape is a triangle, it will have 3 vertices
        if len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            # shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
            shape = 'rectangle'
        # return the name of the shape
        return shape

    def filterContors(self, contours):
        new_contours = []
        for c in contours:
            shape = self.detectShape(c)
            area = cv2.contourArea(c)
            if 2000 < area < 20000 and shape == 'rectangle':
                new_contours.append(c)
        return new_contours

    def detectAndDraw(self, image, contours=None):
        if contours is None:
            contours = self.getColorContours(image)

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(image, self.color, (x + 10, y + 44), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))


if __name__ == "__main__":
    print("color object detection")
