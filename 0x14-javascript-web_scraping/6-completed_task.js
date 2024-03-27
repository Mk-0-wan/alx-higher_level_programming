#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let results = {};
    let json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      let task = json[i];
      if (task.completed === true) {
        if (results?.task?.userId !== undefined) {
          results?.task?.userId += 1;
        } else {
          results?.task?.userId = 1;
        }
      }
    }
    console.log(results);
  }
});
