from flask import Flask
from sand_simulation import Display

app = Flask(__name__)
display = Display()


@app.route("/")
def get_base():
	display.randomify_pixels()
	return f'{display.get_pixels_ds()}'
