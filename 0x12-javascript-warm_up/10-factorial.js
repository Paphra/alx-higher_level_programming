#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  }

  return a * factorial(a - 1);
}

console.log(factorial(num));
