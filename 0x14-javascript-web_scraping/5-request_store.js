#!/usr/bin/node
const fileSystem = require('fs');
const axios = require('axios');
const url = process.argv[2];
const file = process.argv[3];
let dataToWrite = '';
axios.get(url)
  .then(function (response) {
    dataToWrite = response.data;
    fileSystem.writeFile(file, dataToWrite, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  });
