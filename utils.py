import sys
import time
import pyautogui

colors = {
    "CYAN" : "\033[1;36m",
    "GREEN" : "\033[0;32m",
    "RESET" : "\033[0;0m",
    "YELLOW" : "\033[33m"
}

X_MOUSE = 505
Y_MOUSE = 977

def move_mouse_to_initial_position():
    pyautogui.moveTo(X_MOUSE, Y_MOUSE, duration = 1)

def click():
    pyautogui.click()

def enter():
    pyautogui.press("enter") 

def write(text: str):
    pyautogui.write(text)

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