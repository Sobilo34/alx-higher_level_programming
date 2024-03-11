#!/usr/bin/node

const arrayNum = process.argv.slice(2);
function secBiggest (array) {
  if (array.length < 2) {
    return 0;
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return array.pop();
  }
}
console.log(secBiggest(arrayNum));
