import numpy as np
import cv2

class Detect_Color:
	def __init__(self, frame, range_lower, range_upper, area, name, bgr):
		self.frame = frame 
		self.hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
		self.range_lower = np.array(range_lower, np.uint8)
		self.range_upper = np.array(range_upper, np.uint8)
		self.color_mask = cv2.inRange(self.hsvFrame, self.range_lower, self.range_upper)
		self.kernel = np.ones((5, 5), "uint8")
		self.area = area
		self.name = name 
		self.bgr = bgr
		self.contours, self.hierarchy = cv2.findContours(self.color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(self.contours):
			self.area = cv2.contourArea(contour)
			if (self.area > 300):
				x, y, w, h = cv2.boundingRect(contour)
				self.frame = cv2.rectangle(self.frame, (x, y), (x + w, y + h), self.bgr, 2)
				cv2.putText(self.frame, self.name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, self.bgr)
