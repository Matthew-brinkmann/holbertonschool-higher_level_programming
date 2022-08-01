#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occuranceCount = 0;
  for (const item of list) {
    if (item === searchElement) {
      occuranceCount++;
    }
  }
  return (occuranceCount);
};
