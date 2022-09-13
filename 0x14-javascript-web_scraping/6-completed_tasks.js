#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
const CompletedDict = {};
axios.get(url)
  .then(function (response) {
    const totalTasks = response.data.length;
    for (let i = 0; i < totalTasks; i++) {
      const currentTask = response.data[i];
      if (currentTask.completed === true) {
        if (CompletedDict[currentTask.userId] !== undefined) {
          CompletedDict[currentTask.userId] += 1;
        } else {
          CompletedDict[currentTask.userId] = 1;
        }
      }
    }
    console.log(CompletedDict);
  }).catch(function (error) {
    console.log(error.response.status);
  });
