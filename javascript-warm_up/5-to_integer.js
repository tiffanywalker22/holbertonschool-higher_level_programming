#!/usr/bin/node
const args = process.argv;
const ints = parseInt(args[2]);

if (isNaN(ints)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${ints}`);
}
