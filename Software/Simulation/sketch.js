let car;
let obstacles = [];
function setup(){
  createCanvas(800, 800);
  background(0);
  car = new Car(300, height - 150);
  obstacles.push(new Obstacle(createVector(50, height-50), createVector(100, 100)));
  obstacles.push(new Obstacle(createVector(width-50, height-50), createVector(100, 100)));
}

function draw(){
  background(0);
  if(frameCount > 100){
    if(frameCount == 110){
      car.startCurve();
    }
    else if(frameCount < 110){car.braking = true;}
  }
  car.drive();
  car.render();
  for(o of obstacles){
    o.render();
  }
}