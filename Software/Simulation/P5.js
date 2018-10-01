let car;
let obstacles = [];
function setup(){
  createCanvas(800, 800);
  background(0);
  car = new Car(100, height - 200);
  obstacles.push(new Obstacle(createVector(0, height-100), createVector(100, 100)));
  obstacles.push(new Obstacle(createVector(width-100, height-100), createVector(100, 100)));
}

function draw(){
  background(0);
  car.drive();
  car.render();
  for(o of obstacles){
    o.render();
  }
}

class Obstacle{
  constructor(pos, dimensions){
    this.pos = pos;
    this.dimensions = dimensions;
  }
  render(){
    fill("green");
    rect(this.pos.x, this.pos.y, this.dimensions.x, this.dimensions.y);
  }
}

class Car{
  constructor(x, y){
    this.pos = createVector(x,y);
    this.dimensions = createVector(30, 100);
    this.maxspeed = 2;
    this.vel = createVector(1, 0);
    this.acc = createVector(0, 0);
    this.angle  = this.vel.heading() - 0.5 * PI;
    this.color  = "red";
    this.state = 0;
    this.curveVector = createVector(0, 0);
  }
  drive(){
    this.vel.add(this.acc);
    this.vel.limit(this.maxspeed);
    this.angle  = this.vel.heading() - 0.5 * PI;
    this.pos.add(this.vel);
  }
  render(){
    push()
    translate(this.pos.x, this.pos.y);
    rotate(this.angle);
    fill(this.color);
    rect(-this.dimensions.x/2, -this.dimensions.y/2, this.dimensions.x, this.dimensions.y);
    fill("green");
    ellipse(0, 0, 10, 10);
    fill("yellow");
    rect(-this.dimensions.x/2 - 20, this.dimensions.y/2,15, 40);
    pop();
  }
}