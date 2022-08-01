#!/usr/bin/node
const squareSize = process.argv[2];
let currentLineIdx = 0;
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  while (currentLineIdx < squareSize) {
    console.log('X'.repeat(squareSize));
    currentLineIdx++;
  }
}
