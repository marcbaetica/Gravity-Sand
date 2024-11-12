from time import sleep
from pprintpp import pprint
from sand_simulation import DisplayMatrix


# game = DisplayMatrix()
#
# for _ in range(20):
#     pprint(game.get_pixels_ds())
#     game.act_gravity_step()
#     sleep(0.25)




# later: https://docs.bokeh.org/en/latest/docs/user_guide/server/library.html#ug-server-library


from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc

from time import sleep


game = DisplayMatrix()
pixels_matrix = game.get_pixels_ds()
pprint(pixels_matrix)
one_r, one_c = game.get_coordinates_of_one()
print(one_r, one_c)



# create a plot and style its properties
plt = figure(width=2550, height=1250, x_range=(-0.5, 20), y_range=(-0.5, 20), x_axis_label='x')
render_obj = plt.scatter(x=[one_c], y=[20-one_r])  # 20-one_r to inverse it as per the print.

plot_data_struct = render_obj.data_source

# create a callback that adds a number in a random location
def callback():
    game.act_gravity_step()

    # BEST PRACTICE --- update .data in one step with a new dict
    new_data = dict()
    new_data['x'] = plot_data_struct.data['x']
    r, _ = game.get_coordinates_of_one()
    new_data['y'] = [20-r]
    plot_data_struct.data = new_data


# # add a button widget and configure with the call back
# button = Button(label="Press Me")
# button.on_event('button_click', callback)
#
# # put the button and plot in a layout and add to the document
# curdoc().add_root(column(button, plt))


# add a button widget and configure with the call back
button = Button(label="Press Me")
button.on_event('button_click', callback)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, plt))


# bokeh serve --show simulator_runner.py
