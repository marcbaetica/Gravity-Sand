// npm start


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


// Below is an alternative to leveraging var server = http.createServer(app)
app.listen(app.get('port'))

