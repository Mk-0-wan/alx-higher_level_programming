#!/usr/bin/node

if (process.argv[2]) {
  const myVar = process.argv[2];
  if (/^\d+$/.test(myVar) || /^\d+\.\d+$/.test(myVar)) {
    let iter = 0;
    while (iter < myVar) {
      console.log('C is fun');
      iter++;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
