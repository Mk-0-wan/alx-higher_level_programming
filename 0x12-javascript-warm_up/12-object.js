#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// all javascript objects are mutable
myObject.value = 89;
console.log(myObject);
