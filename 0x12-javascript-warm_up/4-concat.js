#!/usr/bin/node
let first;
let second;
if (process.argv[2] || (process.argv[2] && process.argv[3])) {
  first = process.argv[2];
  second = process.argv[3];
}
console.log(first + ' is ' + second);
