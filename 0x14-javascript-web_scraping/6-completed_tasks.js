#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch Data');
  } else {
    try {
      const tasks = JSON.parse(body);
      const completed = {};
      tasks.forEach((task) => {
        if (task.completed) {
          if (completed[task.userId]) {
            completed[task.userId]++;
          } else {
            completed[task.userId] = 1;
          }
        }
      });
      console.log(completed);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
