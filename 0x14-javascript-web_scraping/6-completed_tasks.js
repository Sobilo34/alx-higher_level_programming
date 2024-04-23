#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);

  const result = {};

  for (const todo of data) {
    if (todo.completed) {
      if (result[todo.userId] === undefined) {
        result[todo.userId] = 1;
      } else {
        result[todo.userId] += 1;
      }
    }
  }

  console.log(result);
});
