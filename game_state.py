GRID_W, GRID_H = 100, 100
CUBE_L = 10     # pix

pos_x = int(GRID_W/2)
pos_y = int(GRID_H/2)

directions = ['up', 'down', 'left', 'right']


def adjust_position(direction):
    global pos_x, pos_y
    if not direction in directions:
        raise ValueError(f'Direction value must be one of {directions}.')
    elif direction == 'up':
        pos_y += 1
    elif direction == 'down':
        pos_y -= 1
    elif direction == 'left':
        pos_x -= 1
    elif direction == 'right':
        pos_x += 1
    print(direction)
    print_position()
    return pos_x, pos_y


def print_position():
    print(f'({pos_x}, {pos_y})')


def run_scenario():
    from random import randint
    for i in range(5):
        adjust_position(directions[randint(0, 3)])


run_scenario()

import queue

print(dir(queue.LifoQueue))

