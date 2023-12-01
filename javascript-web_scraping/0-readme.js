#!/usr/bin/node
const fs = require('fs').promises;
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8')
  .then(content => console.log(content))
  .catch(error => console.error(error));
