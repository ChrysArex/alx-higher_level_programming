#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
function process (x, y) {
  return x * y;
}
console.log(list.map(process));
