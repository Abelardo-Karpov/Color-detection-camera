import numpy as np
import cv2
from Detect_Color_03 import Detect_Color

webcam = cv2.VideoCapture(0) # 0 is default camera id, increase it gradually for selecting your desired camera
while True:
	_, frame = webcam.read()

	red = Detect_Color(frame, [170, 130, 100], [180, 255, 255], 800, "Red", (0,0,255))
	blue = Detect_Color(frame, [110, 180, 0], [116, 255, 255], 800, "Blue", (255,0,0))
	green = Detect_Color(frame, [40, 150, 20], [70, 255, 255], 800, "Green", (0,255,0))
	orange = Detect_Color(frame, [2.5, 140, 100], [13, 255, 255], 800, "Orange", (6, 100, 255))
	yellow = Detect_Color(frame, [17.5, 100, 100], [30, 255, 255], 800, "Yellow", (6, 255, 255))
	cyan = Detect_Color(frame, [95, 112, 120], [108, 255, 255], 800, "Cyan", (255, 255, 0))
	purple = Detect_Color(frame, [118, 100, 100], [130, 255, 255], 800, "Purple", (128, 0, 128))
	black = Detect_Color(frame, [0, 0.2, 0.2], [0, 32, 32], 800, "Black", (0, 2, 2))
	pink = Detect_Color(frame, [135, 100, 100], [160, 255, 255], 800, "Pink", (255, 0, 255))
	gray = Detect_Color(frame, [0, 0, 0], [80, 80, 80], 800, "Gray", (128, 128, 128))

	cv2.imshow("Color Detection", frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		webcam.release()
		cv2.destroyAllWindows()
		break
