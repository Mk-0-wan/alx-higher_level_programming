#!/usr/bin/node
/* Getting the reverse order of a string */
exports.esrever = function (list) {
  const emptyList = [];
  const lastIndex = (list.length - 1);

  for (let i = lastIndex; i >= 0; i--) {
    emptyList.push(list[i]);
  }
  return (emptyList);
};
