#!/usr/bin/node
const args = process.argv;
const ints = parseInt(args[2]);

if (isNaN(ints)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < ints; i++) {
    console.log('C is fun');
  }
}
