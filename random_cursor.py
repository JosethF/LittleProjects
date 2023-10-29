import ctypes
import time
import random

user32 = ctypes.windll.user32

# Obtiene el tamaño de la pantalla
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# Mueve el cursor del mouse aleatoriamente
while True:
    x = random.randint(0, width)
    y = random.randint(0, height)
    user32.SetCursorPos(x, y)
    time.sleep(0.5)

    # Si se detecta un clic del botón izquierdo del mouse, se detiene el programa
    if user32.GetAsyncKeyState(0x01) != 0:
        break
