import random
import datetime

from utils import move_mouse_to_initial_position, click, enter, write, print_progress, print_color, sleep

MIN_WAIT_HUMAN = 2
MAX_WAIT_HUMAN = 3

CARD = "vntg72h"
SWAP_CARDS = ["v2w9874", "vkhpflz", "gpfzlw", "vbvbgfk", "vjvsp03", "vw51ttf", "vn781fg"] #[ed1, ed2, ed3, ed4, ed5, ed6, ed7] 
# quality must be 4 -> mint

def swap():
    move_mouse_to_initial_position()

    click()

    wait_time = 0
    human_wait = []
    for key in range(0,len(SWAP_CARDS)):
        wait_h = random.randint(MIN_WAIT_HUMAN*100, MAX_WAIT_HUMAN*100)/100

        wait_time += wait_h
        human_wait.append(wait_h)
        
    now = datetime.datetime.now()

    print_color(f'Hora de inicio: {now.strftime("%H:%M:%S")}\nHora estimada de fin: {(now + datetime.timedelta(0,wait_time)).strftime("%H:%M:%S")}\nTiempo estimado: {round(wait_time/60, 2)}m', "CYAN")

    for key, f in enumerate(SWAP_CARDS):
        write(f"ku swap orb {CARD} frame {f}")

        sleep(human_wait[key])

        enter()

        print_progress(key+1, len(SWAP_CARDS))


if __name__ == '__main__':
    swap()