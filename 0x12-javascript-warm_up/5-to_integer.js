#!/usr/bin/node

const argv = process.argv;
const first = argv[2];

const num = parseInt(first);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
