#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

try {
  const content = fs.readFileSync(filepath, 'utf-8');
  console.log(content);
} catch (error) {
  console.error(error);
}
