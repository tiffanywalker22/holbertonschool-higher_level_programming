#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, function (error) {
    if (error) throw error;
  });
});
