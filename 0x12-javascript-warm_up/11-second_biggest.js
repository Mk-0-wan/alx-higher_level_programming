#!/usr/bin/node

const array = process.argv.slice(2);
if ((array.length === 0) || (array.length === 1)) {
  console.log(0);
} else {
  // convert each of the arguments into an integer
  const sortedArray = array.map(Number).sort((a, b) => a - b);
  // grab the second last element in the sorted array
  const secondLast = (sortedArray.length - 2);
  console.log(sortedArray[secondLast]);
}
