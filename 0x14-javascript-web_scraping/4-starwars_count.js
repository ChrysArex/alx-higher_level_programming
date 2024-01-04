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
      if (perso[perso.length - 3] === '1' && perso[perso.length - 2] === '8') {
        count++;
      }
    }
    );
  }
  );
  console.log(count);
});
