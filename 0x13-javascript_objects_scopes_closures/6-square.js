#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let repr;
    let ligne = '';
    if (c) {
      repr = c;
    } else {
      repr = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        ligne += repr;
      }
      console.log(ligne);
      ligne = '';
    }
  }
}
module.exports = Square;
