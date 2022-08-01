#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (this.validatePositiveIntegers(w, h)) {
      this.width = w;
      this.height = h;
    }
  }

  validatePositiveIntegers (a, b) {
    if (a > 0 && b > 0) {
      return (true);
    }
    return (false);
  }
}

module.exports = Rectangle;
