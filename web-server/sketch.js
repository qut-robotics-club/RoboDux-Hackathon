let points = [];
let pendown = false
let livemode = false

let socket = new WebSocket("ws://localhost:8000");

socket.onopen = function(e) {
  console.log("SHE WORKS BWOIIIIIIIIII")
};

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(220);
  // socket.emit("test")
}

function draw() {
  if(mouseIsPressed) {
    line(prevX, prevY, mouseX, mouseY);
  }
  prevX = mouseX;
  prevY = mouseY;
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  background(220);
}

function mousePressed() {
  pendown = true
}

function mouseReleased() {
  pendown = false
}