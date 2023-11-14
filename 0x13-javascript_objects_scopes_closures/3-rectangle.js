#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ligne = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        ligne += 'X';
      }
      console.log(ligne);
      ligne = '';
    }
  }
}
module.exports = Rectangle;
