let d  = new Date();
// alert("Today's date is " + d);
console.log(d);
document.body.innerHTML = "<h1> Today's date is " + d + "</h1>";

// const socket = io('ws://localhost:9999');
const socket = io('http://localhost:9999');

socket.emit('Hello', 'server!');

socket.on('connection', (socket) => {
  console.log('socket is connected!');
  socket.on('disconnect', () => {
    console.log('socket is disconnected!')
  })
})

