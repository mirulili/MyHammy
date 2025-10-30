### analysis/drinking.py ###
### Btter stay hydrated..###
import time
import datetime
import cv2

WATER_BOWL_ROI = (100, 100, 50, 50)	# Customed position of water bowl
MIN_DRINKING_CONTOUR_AREA = 30 # Constant for minimum contour area
DRINKING_DURATION_THRESHOLD = 10 # Constant for drinking duration threshold
MOVEMENT_RESET_THRESHOLD = 3 # Constant for movement reset threshold (if needed)

def detect_drinking(frame_diff, movement_start_time: float = None) -> (bool, float): 
	x, y, w, h = WATER_BOWL_ROI

	roi_diff = frame_diff[y:y+h, x:x+w]

	# Check if it is staying at the site
	contours, _ = cv2.findContours(roi_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	current_time = time.time()
	for contour in contours:
		if cv2.contourArea(contour) > MIN_DRINKING_CONTOUR_AREA: # Using constant
			if movement_start_time is None:
				movement_start_time = current_time # Use current_time
			elif (current_time - movement_start_time) > DRINKING_DURATION_THRESHOLD:	# Using constant
				print(f"[{datetime.datetime.now()}] Detected drinking movement!")
				return True, None # Return None to reset start time after detection
			break
	else: 
		# No significant contour found in ROI
		# If there was movement_start_time but no current movement, reset it after a short period
		if movement_start_time is not None and (current_time - movement_start_time) > MOVEMENT_RESET_THRESHOLD:
			movement_start_time = None
	
	return False, movement_start_time # Return movement_start_time for persistence