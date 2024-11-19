console.log('connecting to the socket')
const c_soc = new WebSocket('ws://localhost:8500')
console.log(c_soc)  // TODO: A property checks if connection was establshed.

console.log('Sending hello server!')
c_soc.addEventListener('open', function (event) {
  c_soc.send('Hello Server!')
})

c_soc.addEventListener('message', function (event) {
  console.log(c_soc)
  console.log(`Message from server:\n${event.data}`)
  console.log(c_soc)
  var grain_position = eval(event.data)
  ctx.fillRect(grain_position[0], grain_position[1], 10, 10)
})

// socket.on('')


const canvas = document.getElementById('section_map');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'red';
ctx.fillRect(395, 395, 10, 10);

window.addEventListener('keydown', check, false);


function check(e) {
  // 'w' = e.code:87, key:w and e.code:KeyW
  console.log(`Pressed key ${e.code}. Sending to server...`)
  c_soc.send(e.code)
}

