#!/usr/bin/node
const request = require('request');
const charId = 18;
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgemovies = films.filter(film =>
      film.characters.includes(`https://swapi-api.hbtn.io/api/people/${charId}/`)
    );
    console.log(wedgemovies.length);
  }
});
