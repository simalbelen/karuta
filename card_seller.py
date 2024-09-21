import random
import datetime

from utils import move_mouse_to_initial_position, click, enter, write, print_progress, print_color, sleep

MIN_WAIT_HUMAN = 1
MAX_WAIT_HUMAN = 2

MIN_WAIT_COOLDOWN = 13
MAX_WAIT_COOLDOWN = 15

CARDS = ["vbblh44"]

def card_seller():
    move_mouse_to_initial_position()
    click()

    wait_time = 0
    human_wait = []
    cooldowns = []
    for key in range(0,len(CARDS)):
        wait_h = random.randint(MIN_WAIT_HUMAN*100, MAX_WAIT_HUMAN*100)/100
        wait_c = random.randint(MIN_WAIT_COOLDOWN*100, MAX_WAIT_COOLDOWN*100)/100

        wait_time += wait_h + wait_c
        human_wait.append(wait_h)
        cooldowns.append(wait_c)
        
    now = datetime.datetime.now()

    print_color(f'Hora de inicio: {now.strftime("%H:%M:%S")}\nHora estimada de fin: {(now + datetime.timedelta(0,wait_time)).strftime("%H:%M:%S")}\nTiempo estimado: {round(wait_time/60, 2)}m', "CYAN")

    for key, c in enumerate(CARDS):
        write(f"kv {c}")

        sleep(human_wait[key])

        enter()

        print_progress(key+1, len(CARDS))
        
        sleep(cooldowns[key])

if __name__ == '__main__':
    card_seller()