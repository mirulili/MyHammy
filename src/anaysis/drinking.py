### analysis/drinking.py ###
### Btter stay hydrated..###
import time
import datetime

WATER_BOWL_ROI = (100, 100, 50, NULL)	# Actual waterbottle position

def detect_drinking(frame_diff):
	x, y, w, h = WATER_BOWL_ROI

	roi_diff = frame_diff[y:y+h, x:x+w]

	# Check if it is staying at the site
	contours, _ = cv2.findContours(roi_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	movement_start_time = None
	for contour in contours:
		if cv2.contourArea(contour) > 30:
			if movement_start_time is None:
				movement_start_time = time.time()
			elif (time.time() - movement_start_time) > 10:	# If stayed more than 10 sec.
				print(f"[{datetime.datetime.now()}] Detected drinking movement!")
				return True
			break

	if movement_start_time is not None and (time.time() - movement_start_time) < 3:
		pass 

	return False