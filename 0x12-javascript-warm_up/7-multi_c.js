#!/usr/bin/node
const numOfTimesToPrint = process.argv[2];
let printItteration = 0;
if (isNaN(numOfTimesToPrint)) {
  console.log('Missing number of occurrences');
} else {
  while (printItteration < numOfTimesToPrint) {
    console.log('C is fun');
    printItteration++;
  }
}
