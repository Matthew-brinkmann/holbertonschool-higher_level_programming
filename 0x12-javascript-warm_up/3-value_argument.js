#!/usr/bin/node
const argToPrint = process.argv[2];
if (argToPrint === undefined) {
  console.log('No argument');
} else {
  console.log(argToPrint);
}
