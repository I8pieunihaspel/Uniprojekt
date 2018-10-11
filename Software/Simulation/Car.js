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
      this.curving = false;
      this.iT = 0;
      this.braking = false; 
    }
    brake(l){
      this.acc = this.vel.copy().mult(-0.5);
      this.acc.limit(l);
    }
    startCurve(){
      this.iT = frameCount;
      this.braking = false;
      this.curving = true;
    }
    reverseCurve(){ 
      if(this.vel.heading()<= 0 && (frameCount - this.iT) >= 50){
        this.vel = createVector(-0.5, 0);
        this.acc = createVector(0, 0);
        this.curving = false;
  
      }
      else if(frameCount - this.iT <= 50){
        this.vel.x = -0.5;
        this.acc.y = 0.05;
      }
      else {
        this.vel.x = -0.5;
        this.acc.y = -0.05;
      }
    }
    drive(){
      if(this.braking){
        this.brake(1);
      }
      if(this.curving){
        this.reverseCurve();
      }
      this.vel.add(this.acc);
      this.vel.limit(this.maxspeed);
      this.angle = this.vel.heading() - 0.5 * PI;
      this.pos.add(this.vel);
    }
    render(){
      push();
      translate(this.pos.x, this.pos.y);
      rotate(this.angle);
      fill(this.color);
      rect(-this.dimensions.x/2, -this.dimensions.y/2, this.dimensions.x, this.dimensions.y);
      fill("green");
      ellipse(0, 0, 10, 10);
      fill("purple");
      rect(-this.dimensions.x/1.25 - 2, this.dimensions.y/5, 10, 20);
      rect(this.dimensions.x/1.25 - 8.2, this.dimensions.y/5, 10, 20); 
      rect(-this.dimensions.x/1.7 - 8.2, -this.dimensions.y/2.4, 10, 20);
      rect(this.dimensions.x/1.25 - 8.2, -this.dimensions.y/2.4, 10, 20);
      pop();
    }
  }