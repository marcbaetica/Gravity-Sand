from random import randint


class DisplayMatrix:
    pixels = None

    def __init__(self):
        self.randomify_pixels()

    def get_pixels_ds(self):
        assert self.pixels is not None, "Expected self.pixels to not be none!"
        return self.pixels

    def randomify_pixels(self):
        self.pixels = [[0 for _ in range(20)] for _ in range(20)]
        self.pixels[randint(0, len(self.pixels))][randint(0, len(self.pixels[0]))] = 1

    def move_down(self):
        self.pixels.insert(0, self.pixels.pop())

    def act_gravity_step(self):
        # find one
        for r in range(len(self.pixels)):
            for c in range(len(self.pixels[r])):
                if self.pixels[r][c] == 1:
                    coordinates = (r, c)
                    print(f'One at {coordinates}. len(self.pixels)={len(self.pixels)}.')
        if coordinates[0] == len(self.pixels)-1:  # bottom
            pass
        else:
            self.pixels[coordinates[0]][coordinates[1]] = 0
            self.pixels[coordinates[0]+1][coordinates[1]] = 1
