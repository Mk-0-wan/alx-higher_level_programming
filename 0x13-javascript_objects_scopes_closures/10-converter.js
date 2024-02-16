#!/usr/bin/node

exports.converter = function (base) {
  return function (data) {
    return (data.toString(base));
  };
};
