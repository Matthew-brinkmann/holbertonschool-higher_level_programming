#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
axios.get(url)
  .then(function (response) {
    console.log('code: ' + response.status);
  }).catch(function (error) {
    console.log('code: ' + error.response.status);
  });
