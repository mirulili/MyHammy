# My Hammy! 🐹

This is a hamster motion detection project by @mirulili.
The goal of this project is to analyze hamster behavior by tracking its motion, in order to provide insights and care recommendations for hamster well-being.

## Project Structure & File Descriptions

This project consists of several modules for detecting and recording hamster activities.

### `src/main.py`
*   The main executable file of the project.
*   It captures video through a webcam and analyzes the difference between frames to detect the hamster's overall movement.
*   It calls functions from the `analysis` module to detect specific activities like wheel spinning and drinking, and saves the activity logs to the database via the `data` module.

### `src/analysis/wheel_spin.py`
*   Contains the logic for detecting hamster wheel movement.
*   It determines that the wheel is spinning when movement is detected within a specific Region of Interest (ROI) and tracks the total spinning time.

### `src/analysis/drinking.py`
*   Contains the logic for detecting when the hamster is drinking water.
*   It determines that the hamster is drinking if movement persists for a certain duration in a specific Region of Interest (ROI) around the water bottle.

### `src/data/database.py`
*   Provides functions to interact with the SQLite database.
*   It is responsible for initializing the database and saving the hamster's activity logs (e.g., movement, wheel spinning, drinking).
