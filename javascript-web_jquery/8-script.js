#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (responsedata) {
  $.each(responsedata.results, function (i, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
