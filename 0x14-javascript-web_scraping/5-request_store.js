#!/usr/bin/node
const re = require('request');
const fs = require('fs');
re(process.argv[2], function (a, b, c) {
  if (a) {
    return;
  }
  fs.appendFile(process.argv[3], c, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
