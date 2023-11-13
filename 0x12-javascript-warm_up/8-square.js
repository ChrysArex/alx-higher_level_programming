#!/usr/bin/node
const num = parseInt(process.argv[2]);
let square = '';
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
