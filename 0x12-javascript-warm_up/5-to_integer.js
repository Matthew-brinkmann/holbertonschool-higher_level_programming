#!/usr/bin/node
const argToConvToNumber = process.argv[2];
if (isNaN(argToConvToNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argToConvToNumber, 10));
}
