#!/usr/bin/node
const fileToReadOne = process.argv[2];
const fileToReadTwo = process.argv[3];
const fileToWrite = process.argv[4];
const fs = require('fs');
// let dataToWrite;

fs.readFile(fileToReadOne, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  // dataToWrite = data;
  fs.readFile(fileToReadTwo, 'utf8', (err1, data1) => {
    if (err1) {
      console.log(err1);
      return;
    }
    // dataToWrite = dataToWrite + data1;
    fs.writeFile(fileToWrite, data + data1, err2 => {
      if (err2) {
        console.log(err2);
      }
    });
  });
});
