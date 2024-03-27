#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = JSON.parse(body);
    console.log(newObject.title);
  }
});
