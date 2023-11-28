#!/usr/bin/node
const fivesquare = require('./5-square.js');

class Square extends fivesquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
