from lib.constants import GRAIN_MASS
from lib.sand import SandGrain


class ForceVector():
    def __init__(self, i, j):
        self.i = i  # x
        self.j = j  # y

    def __str__(self):
        return f'{self.i}i+{self.j}j'


def accelerate_direction(grain: SandGrain):
    i, j = 0, 0
    # TODO: add this up more efficiently
    for force in grain.forces():
        i += force[0]
        j += force[1]
    return i/GRAIN_MASS, j/GRAIN_MASS
