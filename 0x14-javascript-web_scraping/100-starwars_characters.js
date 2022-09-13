#!/usr/bin/node
const movieId = process.argv[2];
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + movieId)
  .then(function (response) {
    const totalCharacters = response.data.characters.length;
    for (let i = 0; i < totalCharacters; i++) {
      axios.get(response.data.characters[i])
        .then(function (character) {
          console.log(character.data.name);
        });
    }
  });
