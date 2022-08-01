#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (this.validatePositiveIntegers(w, h)) {
      this.width = w;
      this.height = h;
    }
  }

  print (printChar = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }

  rotate () {
    const holdWidth = this.width;
    this.width = this.height;
    this.height = holdWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  validatePositiveIntegers (a, b) {
    if (a > 0 && b > 0) {
      return (true);
    }
    return (false);
  }
}

module.exports = Rectangle;
