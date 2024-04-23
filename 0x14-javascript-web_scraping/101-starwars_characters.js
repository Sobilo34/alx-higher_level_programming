#!/usr/bin/node

const request = require('request');

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      const characterInfo = JSON.parse(body);
      console.log(characterInfo.name);

      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

const filePath = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filePath;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    printCharacters(data.characters, 0);
  }
});
