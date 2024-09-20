from lib.constants import GRAIN_RADIUS, GRAV_FORCE


class SandGrain():
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.r = GRAIN_RADIUS
        self.forces = [GRAV_FORCE]
        self.inertia = [0, 0]  # in pixels

    def __str__(self):
        return f'x={self.x}, y={self.y}, radius={self.r}, forces={self.forces}'

    def new_position(self):
        # position += inertia (inertia calculated by acceleration)
        pass