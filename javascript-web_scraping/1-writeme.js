#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const towrite = process.argv[3];

try {
  fs.writeFileSync(filepath, towrite, 'utf-8');
} catch (error) {
  console.error(error);
}
