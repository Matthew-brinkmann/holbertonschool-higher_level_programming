#!/usr/bin/node
let retValue = 0;
const commandLineArguments = process.argv.slice(2);

if (commandLineArguments.length > 1) {
  commandLineArguments.sort(function (a, b) { return a - b; });
  retValue = commandLineArguments[commandLineArguments.length - 2];
}

console.log(retValue);
