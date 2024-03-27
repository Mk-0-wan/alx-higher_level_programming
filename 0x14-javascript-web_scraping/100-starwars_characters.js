#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// https://swapi-api.alx-tools.com/

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = JSON.parse(body);
    const characters = newObject.characters;
    for (let i = 0; i < characters.length; i++) {
      const p = characters[i];
      request(p, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
