from random import randint


class DisplayMatrix:

    def __init__(self):
        self.pixels = self.randomify_pixels()

    def get_pixels_ds(self):
        assert self.pixels is not None, "Expected self.pixels to not be none!"
        return self.pixels

    @staticmethod
    def randomify_pixels():
        pixels_matrix = [[0 for _ in range(20)] for _ in range(20)]
        pixels_matrix[randint(0, len(pixels_matrix)-1)][randint(0, len(pixels_matrix[0])-1)] = 1
        return pixels_matrix

    def move_down(self):
        self.pixels.insert(0, self.pixels.pop())

    def act_gravity_step(self):
        # find one
        r, c = self.get_coordinates_of_one()
        if r == len(self.pixels)-1:  # bottom
            pass
        else:
            self.pixels[r][c] = 0
            self.pixels[r+1][c] = 1

    def get_coordinates_of_one(self):
        for r in range(len(self.pixels)):
            for c in range(len(self.pixels[r])):
                if self.pixels[r][c] == 1:
                    print(f'One at ({r}, {c}). len(self.pixels)={len(self.pixels)}.')
                    return r, c
