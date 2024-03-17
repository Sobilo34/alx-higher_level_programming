#!/usr/bin/node

const firstArg = process.argv[2];

if (!isNaN(parseInt(firstArg)) && parseInt(firstArg) > 0) {
  const size = parseInt(firstArg);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
