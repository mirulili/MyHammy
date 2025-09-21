# main.py
import cv2
import datetime
import os
import time
from data.database import init_database, save_tracking_log
from analysis.wheel_spin import detect_wheel_spin
from analysis.drinking import detect_drinking
# --- Setting ---
HAMSTER_NAME = "Chamkkae"  # Hamster's name
MIN_MOVEMENT_AREA = 500  # Track it if hamster moved more than this (pixel) value.

# --- Utilities ---
def analyze_movement(frame_diff):
    """
    Analyze difference between two frames and sense movement.
    """
    contours, _ = cv2.findContours(frame_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # calculate contour area
        area = cv2.contourArea(contour)
        if area > MIN_MOVEMENT_AREA:
            # Count as hamster moved if larger than minimal area.
            (x, y, w, h) = cv2.boundingRect(contour)
            # TODO: Store position of hamster (x, y, w, h) and analyze further.
            return True, area
            
    return False, 0

def main():
    # Open device (webcam) 0.
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Failed open camera. Check if it is connected.")
        return

    # Read first frame and set it as background.
    ret, frame1 = camera.read()
    if not ret:
        return
    
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame1 = cv2.GaussianBlur(gray_frame1, (21, 21), 0)

    print("Traking started. Ctrl+C to quit.")
    
    try:
        while True:
            # Read next frame and adjust gray scale and blury.
            ret, frame2 = camera.read()
            if not ret:
                break
            
            gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray_frame2 = cv2.GaussianBlur(gray_frame2, (21, 21), 0)

            # Calculate differences between two frames.
            frame_diff = cv2.absdiff(gray_frame1, gray_frame2)
            # If value exceeds certain value, make its pixel white.
            _, threshold_diff = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
            threshold_diff = cv2.dilate(threshold_diff, None, iterations=2)
            
            # Analyze movement.
            is_moving, area = analyze_movement(threshold_diff)
            
            if is_moving:
                # Save log when hamster moves.
                save_tracking_log("Movement", f"Tracked area: {area} pixel")
                
            # Set current frame as previous frame for next loop.
            gray_frame1 = gray_frame2
            
            # Display urrent frame.
            # cv2.imshow('Hamster Tracking', frame2)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

            time.sleep(1)

    except KeyboardInterrupt:
        print("Traking stopped.")
        
    finally:
        # Free resources.
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    init_database()
    main()