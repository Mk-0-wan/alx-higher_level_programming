#!/usr/bin/node

const request = require('request');
const knownId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${knownId}`;

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = JSON.parse(body);
    console.log(newObject.title);
  }
});
