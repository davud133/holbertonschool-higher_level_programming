#!/usr/bin/node

const { argv } = require('node:process');

let first = 0; let second = 0;

if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > first) {
      second = first;
      first = parseInt(argv[i]);
    }
    if(parseInt(argv[i]) > second && parseInt(argv[i]) !== first){
      second = parseInt(argv[i])
    }
  }
  console.log(second);
}
