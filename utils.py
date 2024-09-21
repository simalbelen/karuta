import sys
import time
from pynput.mouse import Button, Controller as m_Controller
from pynput.keyboard import Key, Controller as k_Controller

mouse = m_Controller()
keyboard = k_Controller()

colors = {
    "CYAN" : "\033[1;36m",
    "GREEN" : "\033[0;32m",
    "RESET" : "\033[0;0m",
    "YELLOW" : "\033[33m"
}

X_MOUSE = 462
Y_MOUSE = 1046

def move_mouse_to_initial_position():
    mouse.position= (X_MOUSE, Y_MOUSE)

def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def write(text: str):
    keyboard.type(text)

def print_progress(part, total):
    if (part != total):
        sys.stdout.write(colors["YELLOW"])
        sys.stdout.write("\r{}/{}  {}%".format(part, total, round((((part)/total)*100),2)))
    else:
        sys.stdout.write(colors["GREEN"])
        sys.stdout.write("\r{}/{}  {}%".format(part, total, round((((part)/total)*100),2)))
        print()
    sys.stdout.write(colors["RESET"])

def print_color(contenido, color):
    sys.stdout.write(colors[color]) #RED
    sys.stdout.write("\r{}".format(contenido))
    print()
    sys.stdout.write(colors["RESET"]) #RESET #Recorre las filas de la respuesta  

def sleep(sleep_time):
    time.sleep(sleep_time)