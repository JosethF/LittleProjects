import ctypes
import time
import random

user32 = ctypes.windll.user32

# Get screen size
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Move the cursor randomly
while True:
    x = random.randint(0, width)
    y = random.randint(0, height)
    user32.SetCursorPos(x, y)
    time.sleep(0.5)

    # If it detects two clicks it will stop
    if user32.GetAsyncKeyState(0x01) != 0:
        break
