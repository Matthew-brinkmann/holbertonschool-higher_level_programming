#!/usr/bin/node
const fileSystem = require('fs');
const file = process.argv[2];
fileSystem.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
