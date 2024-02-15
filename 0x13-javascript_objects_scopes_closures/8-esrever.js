#!/usr/bin/node
/*Getting the reverse order of a string */
exports.esrever = function(list)  {
	const lastIndex = (list.length - 1);
	let emptyList = [];

	for (let i = lastIndex; i >= 0; i--) {
		emptyList.push(list[i]);
	}
	console.log(emptyList);
}
