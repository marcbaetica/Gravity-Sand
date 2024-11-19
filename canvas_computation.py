import numpy as np
from random import randint
from websockets.sync.server import serve


def generate_map():
    a = np.zeros((80, 80))
    for _ in range(100):
        a[randint(0, 79)][randint(0, 79)] = 2
    a[5][5] = 1
    print(a)
    print(str(a))
    return a


# def echo(websocket):
    # for key in websocket:
        # websocket.send(str(generate_map()))

import json
from time import sleep


def echo(websocket):
    for _ in range(1):
        sleep(1)
        map = generate_map()
        print(map)
        map_str = json.dumps(map.tolist())
        print(map_str)
        websocket.send(map_str)

with serve(echo, 'localhost', 8500) as s_soc:
    s_soc.serve_forever()

