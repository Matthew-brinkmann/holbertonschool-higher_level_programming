#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
let appearsIn = 0;
let totalMovies = 0;
axios.get(url)
  .then(function (response) {
    totalMovies = response.data.count;
    for (let i = 0; i < totalMovies; i++) {
      const chars = response.data.results[i].characters;
      if (chars.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        appearsIn++;
      }
    }
    console.log(appearsIn);
  }).catch(function (error) {
    console.log(error.response.status);
  });
