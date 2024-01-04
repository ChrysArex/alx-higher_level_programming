#!/usr/bin/node
const re = require('request');
let count = 0;
let id_ = 1;
const result = {};
re(process.argv[2], function (a, b, c) {
  if (a) {
    console.log(a);
    return;
  }
  JSON.parse(c).forEach(function (elmt) {
    if (elmt.userId === id_) {
      if (elmt.completed === true) {
        count++;
      }
    } else {
      if (count > 0) {
        result['' + id_] = count;
      }
      id_ = elmt.userId;
      count = 0;
      if (elmt.completed === true) {
        count++;
      }
    }
  });
  result['' + id_] = count;
  console.log(result);
});
