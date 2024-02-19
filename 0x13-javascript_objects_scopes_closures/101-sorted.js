#!/usr/bin/node

/*
 * A function that returns a sorted dictonary where the values of a dictonary
 * become the keys of the new dict.
 */
// this file will be imported
const oldDict = require('./101-data').dict;

// Creating some global variables
const setValues = new Set();
const filteredListValues = [];
const newObject = Object.create({});

// Mapping the list of values in a uniqe list
for (const key in oldDict) {
  if (Object.prototype.hasOwnProperty.call(oldDict, key)) {
    const val = oldDict[key];
    if (!setValues.has(val)) {
      setValues.add(val);
      filteredListValues.push(val);
    }
  }
}
// console.log(filteredListValues) //=> returns a uniqe list

// Mapping out the new object with the required { key: values } pairs
// where all the keys having the same values are grouped into a list and
// becomes the values of the new created object
// { 1 : [33, 6, 7, 77], ... }
for (let i = 0; i < filteredListValues.length; i++) {
  const valList = [];
  for (const k in oldDict) {
    if (oldDict[k] === filteredListValues[i]) {
      valList.push(k);
    }
  }
  newObject[filteredListValues[i]] = valList;
}
console.log(newObject);
