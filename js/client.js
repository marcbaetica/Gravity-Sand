console.log('connecting to the socket')
const c_soc = new WebSocket('ws://localhost:8500')
console.log(c_soc)

console.log('Sending hello server!')
c_soc.addEventListener('open', function (event) {
  c_soc.send('Hello Server!')
})

c_soc.addEventListener('message', function (event) {
  console.log(c_soc)
  console.log(`Message from server:\n${event.data}`)
  console.log(c_soc)
})

// socket.on('')

