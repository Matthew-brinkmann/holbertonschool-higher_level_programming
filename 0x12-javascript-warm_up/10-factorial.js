#!/usr/bin/node
const argumentToFindFactorial = process.argv[2];
function factorial (numToFindFactorial) {
  if (isNaN(numToFindFactorial) || numToFindFactorial === 1) {
    return (1);
  } else {
    return (numToFindFactorial * factorial(numToFindFactorial - 1));
  }
}
console.log(factorial(parseInt(argumentToFindFactorial)));
