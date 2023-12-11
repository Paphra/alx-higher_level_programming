#!/usr/bin/node

const { argv } = require('node:process');

const arg = argv.at(2);
if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
