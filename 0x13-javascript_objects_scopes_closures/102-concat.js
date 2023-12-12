#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

if (argv.length === 5) {
  try {
    const src1 = argv[2];
    const src2 = argv[3];
    const dest = argv[4];

    const content1 = fs.readFileSync(src1, 'utf8');
    const content2 = fs.readFileSync(src2, 'utf8');
    const contentDest = content1 + content2;
    fs.writeFileSync(dest, contentDest);
  } catch (err) {
    console.log(err);
  }
}
