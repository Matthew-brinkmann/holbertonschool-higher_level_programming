#!/usr/bin/node
const argLineLen = process.argv.length;
if (argLineLen === 2) {
  console.log('No argument');
} else if (argLineLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
