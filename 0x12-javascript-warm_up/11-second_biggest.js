#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let biggest = 0;
  let second = 0;

  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > biggest) {
      second = biggest;
      biggest = num;
    }
    if (num > second && num < biggest) {
      second = num;
    }
  }

  console.log(second);
}
