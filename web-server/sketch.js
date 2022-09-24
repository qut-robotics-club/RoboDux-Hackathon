let points = [[0, 0, false]];
let pendown = false
let livemode = false

let socket = new WebSocket("ws://www.veleriumproject.com:8000");

socket.onopen = function(e) {
  console.log("SHE WORKS BWOIIIIIIIIII")
};

socket.addEventListener('message', function (event) {
 
  // points = event.data["path"]
  // print(event.data)
  points = JSON.parse(event.data).path
  console.log("received comms")

});

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(220);
}

function draw() {
  background(220);
  if(mouseIsPressed) {
    points.push([mouseX, mouseY, true])
  }
  prevX = points[0][0];
  prevY = points[0][1];
  for (let i = 1; i<points.length; i++) {
    if(points[i-1][2]) {
      
      stroke(0)
    }
    else {
      noStroke()
    }
    line(prevX, prevY, points[i][0], points[i][1])
      prevX = points[i][0];
      prevY = points[i][1];
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  background(220);
}

function mousePressed() {
  pendown = true
  points.push([mouseX, mouseY, false])
}

function mouseReleased() {
  pendown = false
  points.push([mouseX, mouseY, false])
  data = {'path': points}
  socket.send(JSON.stringify(data))
  socket.send(JSON.stringify(data))
}