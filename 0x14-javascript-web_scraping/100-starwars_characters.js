#!/usr/bin/node
const re1 = require('request');
const re2 = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
re1(url, function (a, b, c) {
  JSON.parse(c).characters.forEach(function (elmt) {
    re2(elmt, function (e, f, g) {
      console.log(JSON.parse(g).name);
    });
  });
});
