#!/usr/bin/node

const argv = process.argv;
const times = parseInt(argv[2]);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < times) {
    console.log('C is fun');
    count++;
  }
}
