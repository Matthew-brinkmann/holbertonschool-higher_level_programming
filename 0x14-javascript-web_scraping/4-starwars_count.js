#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
let appearsIn = 0;
let totalMovies = 0;
axios.get(url)
  .then(function (response) {
    totalMovies = response.data.results;
    for (const filmNumber in totalMovies) {
      const chars = totalMovies[filmNumber].characters;
      for (const charNumber in chars) {
        if (chars[charNumber].includes('18')) {
          appearsIn++;
        }
      }
    }
    console.log(appearsIn);
  }).catch(function (error) {
    console.log(error);
  });
