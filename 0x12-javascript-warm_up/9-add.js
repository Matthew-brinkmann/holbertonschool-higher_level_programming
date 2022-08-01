#!/usr/bin/node
const integerOne = process.argv[2];
const integerTwo = process.argv[3];
function add (integerOne, integerTwo) {
  if (isNaN(integerOne) || isNaN(integerTwo)) {
    return (NaN);
  } else {
    return (parseInt(integerOne) + parseInt(integerTwo));
  }
}
console.log(add(integerOne, integerTwo));
