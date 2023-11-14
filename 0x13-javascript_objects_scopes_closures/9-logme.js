#!/usr/bin/node
exports.logMe = function () {
  let count = 0;
  console.log('qlqchosz');
  return function logI (val) {
    console.log(count, ':', ' ', val);
    count++;
  };
}
