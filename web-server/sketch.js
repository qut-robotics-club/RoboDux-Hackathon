let points = [];
let pendown = false
let livemode = false
function setup() {
  createCanvas(windowWidth, windowHeight);
  background(220);
  
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