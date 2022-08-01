#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let numOfTimesFuncCalled = 0;
  while (numOfTimesFuncCalled < x) {
    theFunction();
    numOfTimesFuncCalled++;
  }
};
