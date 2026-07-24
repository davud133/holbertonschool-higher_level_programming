#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  if (Number.isNaN(a) || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(parseInt(argv[2])));
