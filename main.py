import requests as req

URL = 'http://127.0.0.1:5000'
for _ in range(10):
    res = req.get(URL)
    print(res.text)
