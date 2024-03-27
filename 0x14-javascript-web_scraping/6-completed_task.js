#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const taskTable = {};
const arr = [];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json?.[i]?.completed === true) {
        const counts = json?.[i]?.userId;
        arr.push(counts);
      }
    }
    arr.forEach(element => {
      taskTable[element] = (taskTable[element] || 0) + 1;
    });
    console.log(taskTable);
  }
});
