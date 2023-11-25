#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const newargs = args.sort((x, y) => y - x);
  console.log(newargs[1]);
}
