### analysis/wheel_spin.py ###
### Track wheel spinning ..###

import cv2
import datetime

WHEEL_ROI = (300, 200, 150, 150)	# Customed position of wheel
MIN_WHEEL_CONTOUR_AREA = 50 # Constant for minimum contour area

def detect_wheel_spin(frame_diff, current_total_wheel_time: int) -> (bool, int):
	x, y, w, h = WHEEL_ROI

	roi_diff = frame_diff[y:y+h, x:x+w]

	contours, _ = cv2.findContours(roi_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	movement_in_wheel = False
	for contour in contours:
		if cv2.contourArea(contour) > MIN_WHEEL_CONTOUR_AREA: 
			movement_in_wheel = True
			break

	if movement_in_wheel:
		updated_total_wheel_time = current_total_wheel_time + 1	# loop by 1 second
		print(f"[{datetime.datetime.now()}] Detected wheel spinning! Total running time: {updated_total_wheel_time}seconds")
		return True, updated_total_wheel_time # Return updated time
	return False, current_total_wheel_time # Return current time if no movement
