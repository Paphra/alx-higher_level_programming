#!/usr/bin/node

exports.converter = function (base) {
  return function convert(number) {
    if (number < base) {
      return String(number);
    } else {
      return convert(Math.floor(number / base)) + String(number % base);
    }
  }
};
