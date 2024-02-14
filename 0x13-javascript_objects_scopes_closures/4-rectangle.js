#!/usr/bin/node

module.exports = class Rectangle {
  width;
  height;

  constructor (w, h) {
    if ((w <= 0) || (h <= 0) || isNaN(w) || isNaN(h)) {
      // just do nothing
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = this.height;
    while (x) {
      console.log('X'.repeat(this.width));
      x--;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
