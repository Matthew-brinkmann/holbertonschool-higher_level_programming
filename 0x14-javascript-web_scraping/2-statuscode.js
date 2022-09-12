#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
axios.get(url)
  .then(function (response, error) {
    if (response) {
      console.log('code: ' + response.status);
    } else {
      console.log('code: ' + error.response.status);
    }
  });
