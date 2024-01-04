#!/usr/bin/node
const re = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
re(url + process.argv[2], function (a, b, c) {
  if (a) {
    return;
  }
  console.log(JSON.parse(c).title);
});
