/* global $  */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, state) {
  data.results.forEach(function (elmt) {
    $('#list_movies').append('<li>' + elmt.title + '</li>');
  });
});
