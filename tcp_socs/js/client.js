// let d  = new Date();
// alert("Today's date is " + d);
// console.log(d);
// document.body.innerHTML = "<h1> Today's date is " + d + "</h1>";


const canvas = document.getElementById('section_map');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'red';
ctx.fillRect(395, 395, 10, 10);

window.addEventListener('keydown', this.check, false);

function send_keystroke_code(data) {
  // console.log(data)
  // console.log(`${data}`)
  const http = new  XMLHttpRequest()
  const url = 'http://localhost:8000/keystroke'
  http.open('POST', url)
  console.log(`sending data ${data}`)
  http.send(data)
  // renew later
  // http.onreadtstatechange=(e) => {
    // if (http.status === 200) {
      // console.log(http.responseText)
      // return true
    // }
  // }
}

function check(e) {
  // alert(e.keyCode)
  // 'w' = e.code:87 and e.code:KeyW
  console.log(e.keyCode)
  send_keystroke_code(e.code)
}

