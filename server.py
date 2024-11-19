from pprintpp import pprint
from websockets.sync.server import serve


grain_pos = [400, 400]

def calculate_new_position(key):
    global GRAIN_POSITION
    acceptable_keys = ['KeyW', 'KeyA', 'KeyS', 'KeyD']
    if key not in acceptable_keys:
        print(f'Key {key} was not in one of the accepted {acceptable_keys}.')
    # TODO: Account for edges.
    elif key == acceptable_keys[0]:
        grain_pos[1] = grain_pos[1] - 10
    elif key == acceptable_keys[1]:
        grain_pos[0] = grain_pos[0] - 10
    elif key == acceptable_keys[2]:
        grain_pos[1] = grain_pos[1] + 10
    elif key == acceptable_keys[3]:
        grain_pos[0] = grain_pos[0] + 10
    return grain_pos


def echo(websocket):
    for key in websocket:
        print(f'Key pressed was: {key}')
        print(f'Sending {grain_pos}.')
        websocket.send(str(calculate_new_position(key)))


with serve(echo, 'localhost', 8500) as s_soc:
    s_soc.serve_forever()

