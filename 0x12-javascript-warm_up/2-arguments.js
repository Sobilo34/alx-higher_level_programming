#!/usr/bin/node

const isArg = process.argv[2];

if (isArg === undefined) {
  console.log('No argument');
} else {
  console.log(isArg);
}
