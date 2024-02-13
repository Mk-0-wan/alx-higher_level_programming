#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  while (x && /^\d+$/.test(x)) {
    theFunction();
    x--;
  }
};
