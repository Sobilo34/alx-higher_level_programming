#!/usr/bin/node
const { dict } = require('./101-data');

const userOccur = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userOccur[occurrence]) {
    userOccur[occurrence] = [];
  }
  userOccur[occurrence].push(userId);
}

console.log(userOccur);
