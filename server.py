from pprintpp import pprint
from websockets.sync.server import serve


def echo(websocket):
    for message in websocket:
        pprint(message)
        websocket.send('Hello Client!')

with serve(echo, 'localhost', 8500) as s_soc:
    s_soc.serve_forever()

