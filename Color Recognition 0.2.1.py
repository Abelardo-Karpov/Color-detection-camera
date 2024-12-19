import numpy as np
import cv2

class Camera:
    def __init__(self):
        pass

    def Assign_Camera(self, _Camera_ID):
        self.Webcam = cv2.VideoCapture(_Camera_ID)

    def Start_Camera(self):
        while (1):
            _, imageFrame = self.Webcam.read()
            hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

            cv2.imshow("Color Detection", imageFrame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                self.Webcam.release()
                cv2.destroyAllWindows()
                break

Camera0 = Camera()
Camera0.Assign_Camera(0)
Camera0.Start_Camera()