#!/usr/bin/node
const fileToReadOne = process.argv[2];
const fileToReadTwo = process.argv[3];
const fileToWrite = process.argv[4];
const fs = require('fs');

fs.readFile(fileToReadOne, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.readFile(fileToReadTwo, 'utf8', (err1, data1) => {
    if (err1) {
      console.log(err1);
      return;
    }
    fs.writeFile(fileToWrite, data + data1, err2 => {
      if (err2) {
        console.log(err2);
      }
    });
  });
});
