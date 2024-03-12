#!/usr/bin/node
const SquareBase = require('./5-square.js');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      let j = 0;
      for (i; i < this.width; i++) {
        let row = '';
        for (j = 0; j < this.height; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
