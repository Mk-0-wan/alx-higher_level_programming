#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  if (x) {
    x++;
    theFunction(x);
  }
};
