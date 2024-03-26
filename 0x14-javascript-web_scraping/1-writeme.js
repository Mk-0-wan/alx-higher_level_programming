#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const data = process.argv[3];

// writing to a file
fs.writeFile(fileName, data, { encoding: 'utf-8' }, err => {
  if (err) { console.log(err); }
});
