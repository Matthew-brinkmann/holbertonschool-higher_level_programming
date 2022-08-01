#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const newDict = {};
for (const key in oldDict) {
  if (newDict[oldDict[key]] === undefined) {
    newDict[oldDict[key]] = [];
  }
  newDict[oldDict[key]].push(key);
}
console.log(newDict);
