import random
import datetime

from utils import move_mouse_to_initial_position, click, enter, write, print_progress, print_color, sleep

MIN_WAIT_HUMAN = 2
MAX_WAIT_HUMAN = 3

FRAME_NAME = "budokai"

CARDS = ["vnj5862", "clbmcj", "vbvbgfk", "vnpfftv", "vj8f4xd", "vkhpflz", "vjd5nfb", "vj595h2", "vk39vdc", "vjklc2g", "vjhj47d", "vjhws98", "vjqkdc5", "vj0dszj", "v5wfcm1", "vb691js", "v5dk3q9", "p3knpr", "3xd6th", "v5hf9fx", "vb326zg", "vb8c53h", "vb8sdcj", "vwbkctq", "vk274h1", "vk5p2bx", "vb30jbr", "v53bxfl", "vkbbgmc", "vk9cfhg", "vb4pxdv", "vw51ttf", "vw4z94h", "vk2c1f2", "v5zzsb1", "v5g1tv9", "v529r9k", "vw7gnrm", "v5vj0gj", "vk6wfsm", "vkhhlvv", "vkw4q72", "v2dxnqh", "vkhdnsk", "v2nf4gv", "vwqsks5", "vw474bg", "3zw0ph", "v229g9j", "v2w9874", "vqfrbn9", "v22bz02" ]
def tester():
    move_mouse_to_initial_position()
    click()

    wait_time = 0
    human_wait = []
    for key in range(0,len(CARDS)):
        wait_h = random.randint(MIN_WAIT_HUMAN*100, MAX_WAIT_HUMAN*100)/100

        wait_time += wait_h
        human_wait.append(wait_h)
        
    now = datetime.datetime.now()

    print_color(f'Hora de inicio: {now.strftime("%H:%M:%S")}\nHora estimada de fin: {(now + datetime.timedelta(0,wait_time)).strftime("%H:%M:%S")}\nTiempo estimado: {round(wait_time/60, 2)}m', "CYAN")

    for key, c in enumerate(CARDS):
        write(f"ku {FRAME_NAME} frame {c}")

        sleep(human_wait[key])

        enter()

        print_progress(key+1, len(CARDS))

if __name__ == '__main__':
    tester()