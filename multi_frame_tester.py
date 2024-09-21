import random
import datetime
from utils import move_mouse_to_initial_position, click, write, enter, print_progress, print_color, sleep

MIN_WAIT_HUMAN = 2
MAX_WAIT_HUMAN = 3

CARD = "l7lfr5"
FRAMES = ["beauty","empyrean","forbidden","glory","karuta anniversary 2024","magitor","midnight bloom","mirrored energy","pastel geometry","smithy forge","springtide serenity","tetromino","wife","year of the boar","year of the dragon","year of the ox","year of the rabbit","year of the tiger", "sea temple"]

def tester():
    move_mouse_to_initial_position()

    click()

    wait_time = 0
    human_wait = []
    for key in range(0,len(FRAMES)):
        wait_h = random.randint(MIN_WAIT_HUMAN*100, MAX_WAIT_HUMAN*100)/100

        wait_time += wait_h
        human_wait.append(wait_h)
        
    now = datetime.datetime.now()

    print_color(f'Hora de inicio: {now.strftime("%H:%M:%S")}\nHora estimada de fin: {(now + datetime.timedelta(0,wait_time)).strftime("%H:%M:%S")}\nTiempo estimado: {round(wait_time/60, 2)}m', "CYAN")

    for key, f in enumerate(FRAMES):
        write(f"ku {f} frame {CARD}")

        sleep(human_wait[key])

        enter()

        print_progress(key+1, len(FRAMES))

if __name__ == '__main__':
    tester()