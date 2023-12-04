#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const taskscomp = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach((task) => {
      if (task.completed) {
        taskscomp[task.userId] = (taskscomp[task.userId] || 0) + 1;
      }
    });
    console.log(taskscomp);
  }
});
