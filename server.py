from websockets.sync.server import serve


def echo(websocket):
    for message in websocket:
        websocket.send(message)

with serve(echo, 'localhost', 8500) as s_soc:
    s_soc.serve_forever()

