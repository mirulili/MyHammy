### analysis/wheel_spin.py ###
### Track wheel spinning ..###

import cv2
import datetime

WHEEL_ROI = (300, 200, 150, 150)	# Actual position of wheel
total_wheel_time = 0

def detect_wheel_spin(frame_diff):
	global total_wheel_time
	x, y, w, h = WHEEL_ROI


	roi_diff = frame_diff[y:y+h, x:x+w]

	contours, _ = cv2.findContours(roi_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	movement_in_wheel = False
	for contour in contours:
		if cv2.contourArea(contour) > 50:
			movement_in_wheel = True
			break

	if movement_in_wheel:
		total_wheel_time += 1	# loop by 1 second
		print(f"[{datetime.datetime.now()}] Detected wheel spinning! Total running time: {total_wheel_time}seconds")
		return True
	return False

