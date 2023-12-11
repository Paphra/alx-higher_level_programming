#!/usr/bin/node

const argv = process.argv;

const first = parseInt(argv[2]);
const second = parseInt(argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(first, second);
