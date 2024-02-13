#!/usr/bin/node

function add (a, b) {
  if (a && b) {
    return (a + b);
  } else {
    return (NaN);
  }
}

const fst = parseInt(process.argv[2]);
const snd = parseInt(process.argv[3]);

console.log(add(fst, snd));
