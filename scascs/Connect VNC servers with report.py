import os
import time
import pyautogui
import pygetwindow as gw
import subprocess
import random

# Function to make a CSV file
def make_csv(filename: str, data, new=True):
    """Make a CSV file with the given filename and enter the data"""
    mode = "w" if new else "a"
    with open(filename, mode, newline="", encoding="utf-8") as f:
        f.write(data)

# Path to the folder containing the VNC files
folder_path = "D:\\pyhton projects\\VNC Script\\VNC Servers"

# Get a list of all VNC files in the folder
vnc_files = [file for file in os.listdir(folder_path) if file.endswith(".vnc")]

# Create the initial CSV file
make_csv("Server Report.csv", "Servers Name,Result\n", new=True)


# Function to move the cursor to the left side of the screen
def move_cursor_to_left():
    screen_width, _ = pyautogui.size()
    pyautogui.moveTo(0, screen_width // 2, duration=1)

# Function to perform random mouse movements within a specified region
def random_mouse_movement():
    screen_width, screen_height = pyautogui.size()
    region_width = screen_width // 2
    region_height = screen_height // 2

    # Define the region boundaries
    x_start = screen_width // 4
    y_start = screen_height // 4
    x_end = x_start + region_width
    y_end = y_start + region_height

    # Perform random mouse movements within the region
    for _ in range(1):
        x = random.randint(x_start, x_end)
        y = random.randint(y_start, y_end)
        pyautogui.moveTo(x, y, duration=0.5)
        # Wait for 1 second
        time.sleep(1)

# Loop through each VNC file
for vnc_file in vnc_files:
    print(vnc_file)
    # Get the file name without extension
    file_name = os.path.splitext(vnc_file)[0]

    # Get the full path of the VNC file
    vnc_file_path = os.path.join(folder_path, vnc_file)

    # Open the VNC file using the default program
    try:
        subprocess.Popen([vnc_file_path], shell=True)
    except:
        make_csv("Server Report.csv", f"{file_name},Connection failed\n", new=False)
        continue


    # Wait for 4 seconds
    time.sleep(4)

    # Move the cursor to the left side of the screen
    move_cursor_to_left()

    # Wait for 3 seconds
    time.sleep(3)

    # Perform random mouse movements within a specified region
    random_mouse_movement()
    # Wait for 4 seconds
    time.sleep(4)

    # Find the VNC viewer window
    vnc_window = gw.getWindowsWithTitle("VNC Viewer")[0]

    # Check if the VNC viewer window is active (connected)
    if vnc_window.isActive:
        make_csv("Server Report.csv", f"{file_name},Connection successful\n", new=False)
    else:
        # Check if any window is present other than the VNC viewer window
        all_windows = gw.getAllTitles()
        if "VNC Viewer" in all_windows:
            all_windows.remove("VNC Viewer")
        
        if all_windows:
            make_csv("Server Report.csv", f"{file_name},Connection failed\n", new=False)
        else:
            make_csv("Server Report.csv", f"{file_name},Connection successful\n", new=False)

    # Wait for 4 seconds
    time.sleep(4)
    # Close the VNC viewer window
    vnc_window.close()

    time.sleep(2)
