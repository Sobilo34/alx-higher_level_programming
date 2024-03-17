#!/usr/bin/node

const firstArg = process.argv[2];

if (parseInt(firstArg)) {
  const x = parseInt(firstArg);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
