#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

if (isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(num1 + num2);
}
