from time import sleep
from pprintpp import pprint
from sand_simulation import DisplayMatrix


# game = DisplayMatrix()
#
# for _ in range(20):
#     pprint(game.get_pixels_ds())
#     game.act_gravity_step()
#     sleep(0.25)


from bokeh.plotting import figure, show
from bokeh.models import glyph


plt = figure(width=2550, height=1250, x_range=(-0.5, 20), y_range=(-0.5, 20), x_axis_label='x')
plt.scatter([0, 1, 2, 3], [1, 6, 8, 9])

show(plt)
