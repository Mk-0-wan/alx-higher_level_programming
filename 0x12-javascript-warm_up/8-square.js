#!/usr/bin/node

if (process.argv[2]) {
  const ssize = process.argv[2];
  if (/^\d+$/.test(ssize)) {
    let iter = 0;
    while (iter < ssize) {
      console.log('X'.repeat(ssize));
      iter++;
    }
  }
} else {
  console.log('Missing size');
}
