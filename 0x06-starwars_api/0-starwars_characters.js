#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  const fetchCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err2, res2, body2) => {
      if (err2) {
        console.error(err2);
        return;
      }
      const name = JSON.parse(body2).name;
      console.log(name);
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
