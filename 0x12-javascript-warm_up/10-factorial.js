#!/usr/bin/node

// check if num is a Number
const num = process.argv[2];
if (isNaN(num)) {
	return 1;
}
// perform the factorial algorithm
function factorial(n) {
	if (n === 0)  {
		return 1;
	} else {
		return n * factorial(n - 1);
	}
}

console.log(factorial(parseInt(num)));
