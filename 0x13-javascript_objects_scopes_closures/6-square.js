#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = this.height;
    while (i) {
      console.log((c.repeat(this.width)));
      i--;
    }
  }
};
