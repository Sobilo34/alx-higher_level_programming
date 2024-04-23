#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  let totalCount = 0;

  for (const film of data.results) {
    const charactersWithWedge = film.characters.filter(character => character.includes('18'));
    totalCount += charactersWithWedge.length;
  }
  console.log(totalCount);
});
