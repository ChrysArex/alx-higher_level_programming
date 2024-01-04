#!/usr/bin/node
const re = require('request');
const url = process.argv[2];
let count = 0;
re(url, function (a, b, c) {
  if (a) {
    return;
  }
  JSON.parse(c).results.forEach(function (elmts) {
    elmts.characters.forEach(function (perso) {
      if (perso === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
    );
  }
  );
  console.log(count);
});
