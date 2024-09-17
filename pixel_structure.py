from random import randint


class Display:
    pixels = None

    def get_pixels_ds(self):
        return self.pixels

    def randomify_pixels(self):
        self.pixels = [[randint(0, 9) for _ in range(3)] for _ in range(3)]
        # self.pixels = [[x for x in range(3)] for y in range(5)]
