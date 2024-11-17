// npm start


// required to actually receive data.
// See https://expressjs.com/en/resources/middleware/body-parser.html
const bodyParser = require('body-parser')
const express = require('express')
const path = require('path')
// const http = require('http')


app = express()
app.set('port', 8000)

app.use(express.static('.'))  // Load js and css libs from folder also.

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'client.html'))
  // res.send(__dirname)
  // console.log(__dirname)
})

app.post('/keystroke', bodyParser.text(), function (req, res) {
  const key_code = req.body
  console.log(`keystroke code received is ${key_code}`)
  // without this, the client (web page) sends payloads,
  // but server stops receiving any more after 7-ish payloads.
  res.status(200).send(`keystorke code was ${key_code}`)
})

// Below is an alternative to leveraging var server = http.createServer(app)
app.listen(app.get('port'))

