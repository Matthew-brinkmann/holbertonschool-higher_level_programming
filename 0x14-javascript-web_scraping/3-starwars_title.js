#!/usr/bin/node
const movieId = process.argv[2];
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + movieId)
  .then(function (response) {
    console.log(response.data.title);
  });
