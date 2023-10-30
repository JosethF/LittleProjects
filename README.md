# Shutdown Timer with Random Cursor

This Python script provides a graphical user interface (GUI) to set a specific time for your computer to automatically shut down. It also includes an option to run a program called `random_cursor.exe` and gives visual cues about the time remaining until shutdown. This script uses the Tkinter library for the GUI and integrates system commands for shutdown functionality.

## Overview

This project offers a simple way to schedule your computer's shutdown time. You can set the desired shutdown time, and optionally, run `random_cursor.exe` before the shutdown occurs. The script provides user-friendly prompts and visual feedback.

## Features

- Set a specific time for automatic system shutdown.
- Option to run `random_cursor.exe` before the shutdown.
- User-friendly graphical interface.

## How to Use

1. **Set Shutdown Time:**
   - Enter the desired shutdown time in 24-hour format (hours and minutes).
   - Click on the "Submit" button or press "Enter" to confirm the shutdown time.
   - Ensure the input time is valid and earlier than the current time.

2. **Optional: Run Random Cursor**
   - Check the "Run Random Cursor" checkbox if you want to run `random_cursor.exe` before shutdown.
   - If checked, `random_cursor.exe` will be executed when the specified time is reached.

3. **Shutdown Process:**
   - Once the time is reached, the script will initiate a system shutdown.
   - If the "Run Random Cursor" option is selected, `random_cursor.exe` will run before shutdown.

## How to Run

**It is important that you have the executable files in this folder, the same with the Python script files.**

**Python Scripts:**

1. Make sure you have Python installed on your system.

2. Make sure you have Tkinter Installed

**Executables:**

1. Nothing is necessary, just have the executable files.

___

# Random Cursor Movement

This Python script moves the cursor randomly across the screen until it detects two mouse clicks, at which point it stops moving the cursor. 

## How to Use

1. **Requirements:**
   - This script is specifically designed for Windows operating systems due to its reliance on the Windows API.
   - Ensure you have Python installed on your system.

2. **Run the Script:**
   - Clone the repository or download `random_cursor.exe`
   - Execute the Python file.
   - The cursor will start moving randomly across the screen.

3. **Stop Cursor Movement:**
   - Click the left mouse button twice to stop the cursor movement.

___

# Executables

In the "executables" folder of this repository, you can find precompiled executable files for this program. If you prefer not to run the program from the source code, you can use the executable specific to your operating system.

- **random_cursor.exe**
- **time_sleeper.exe**