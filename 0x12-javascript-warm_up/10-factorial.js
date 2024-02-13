#!/usr/bin/node

// check if num is a Number
const num = parseInt(process.argv[2], 10);
// perform the factorial algorithm
function factorial (n) {
  if (n === 0 || isNaN(num)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(num));
