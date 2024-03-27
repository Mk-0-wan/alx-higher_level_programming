#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const fileName = process.argv[3];

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = body;
    console.log(newObject);

    fs.writeFile(fileName, newObject, { encoding: 'utf-8' }, err => {
      if (err) { console.log(err); }
    });
  }
});
