#!/usr/bin/node

/*
 * Reading and writing to a file in a synchronous manner.
 * Using open to make a pool that will be able to handle both reading and writig to file.
 * Function will be taking multiple cmd args, will need to use process.argv
 */

//console.log(Object.getPrototypeOf(process.argv));

/*
 * Object is a list type.Open with read and write synchronously, for file one open, file two open for reading
 * then write all the data collected from both the file and write to the third argument. All in the same order.
 */

const fs = require('fs');
const fileA = './fileA';
const fileB = './fileB';

function readFileAHandler (fileA) {
  fs.readFile(fileA, (err, data) => {
    if (err) {
      throw (err);
    }
    const content = data.toString();
    if (content) {
      fs.appendFile('./fileC', content, (err) => {
        if (err) {
          throw (err);
        }
        //console.log('saved');
      });
    }
  });
}

function readFileBHandler (fileB) {
  fs.readFile(fileB, (err, data) => {
    if (err) {
      throw (err);
    }
    const contentB = data.toString();
    if (contentB) {
      fs.appendFile('./fileC', contentB, (err) => {
        if (err) {
          throw (err);
        }
        //console.log('All saved');
      });
    }
  });
}
readFileAHandler(fileA);
readFileBHandler(fileB);
