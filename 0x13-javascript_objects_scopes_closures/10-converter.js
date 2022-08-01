#!/usr/bin/node
exports.converter = function (base) {
  function convertNumber (number) {
    return number.toString(base);
  }
  return convertNumber;
};
