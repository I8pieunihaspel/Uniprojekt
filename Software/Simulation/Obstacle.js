
class Obstacle{
    constructor(pos, dimensions){
      this.pos = pos;
      this.dimensions = dimensions;
    }
    isPointInMe(pos){
        if(this.pos.x-this.dimensions.x/2 <= pos.x && this.pos.x+this.dimensions.x/2 >= pos.x && this.pos.y-this.dimensions.y/2 <= pos.y && this.pos.y+this.dimensions.y/2 >= pos.y){
            print("Hit");
        }
    }
    render(){
      fill("green");
      rect(this.pos.x-this.dimensions.x/2, this.pos.y-this.dimensions.y/2, this.dimensions.x, this.dimensions.y);
    }
  }