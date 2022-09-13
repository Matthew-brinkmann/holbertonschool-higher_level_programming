#!/usr/bin/node
const fileSystem = require('fs');
const file = process.argv[2];
const dataToWrite = process.argv[3];
fileSystem.writeFile(file, dataToWrite, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
