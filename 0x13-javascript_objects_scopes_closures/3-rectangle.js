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
    while (this.height) {
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }
};
