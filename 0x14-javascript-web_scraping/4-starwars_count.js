#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = JSON.parse(body);
    const goingUp = newObject.results;
    let count = 0;
    for (let i = 0; i < newObject.count; i++) {
      const p = goingUp?.[i]?.characters;
      for (let j = 0; j < p.length; j++) {
        if (p[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
