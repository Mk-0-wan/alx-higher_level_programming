#!/usr/bin/node

if (process.argv[2]) {
  const myVar = process.argv[2];
  if (/^\d+$/.test(myVar) || /^\d+\.\d+$/.test(myVar)) {
    console.log(`My number: ${myVar}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
