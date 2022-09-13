#!/usr/bin/node
const movieId = process.argv[2];
const axios = require('axios');
const responseOrder = [];
const responseValue = {};

function getCharacterName (charUrl) {
  axios.get(charUrl)
    .then(function (character) {
      responseValue[charUrl] = character.data.name;
    });
}

axios.get('https://swapi-api.hbtn.io/api/films/' + movieId)
  .then(function (response) {
    const totalCharacters = response.data.characters.length;
    for (let i = 0; i < totalCharacters; i++) {
      responseOrder.push(response.data.characters[i]);
      getCharacterName(response.data.characters[i]);
    }
  });
setTimeout(function () {
  responseOrder.forEach(function (url) {
    console.log(responseValue[url]);
  });
}, 5000);
