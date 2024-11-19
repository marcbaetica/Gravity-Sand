from pprintpp import pprint
from websockets.sync.client import connect


with connect("ws://localhost:8500") as c_soc:
    c_soc.send("Hello world!")
    # print(c_soc)
    # pprint(dir(c_soc))
    message = c_soc.recv()
    # print(message)
    for i in range(10):
        c_soc.send(f'Hello world! {i}')
        msg = c_soc.recv()
        print(msg)


# TODO: Implement with asyncio for larger number of clients.

