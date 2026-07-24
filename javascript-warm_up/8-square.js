#!/usr/bin/node
const { argv } = require('node:process');
const n = parseInt(argv[2]);

if (Number.isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
