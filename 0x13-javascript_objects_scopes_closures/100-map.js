#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((v, i) => v * i);

console.log(list);
console.log(newList);
