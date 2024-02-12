#!/usr/bin/node

const args = process.argv.slice(2);

const argsint = args.map(Number);
argsint.sort((a, b) => b - a);
if (isNaN(argsint[1])) { console.log(0); } else { console.log(argsint[1]); }
