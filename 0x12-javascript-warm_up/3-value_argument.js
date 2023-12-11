#!/usr/bin/node

const argv = process.argv;

const arg = argv.at(2);
if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
