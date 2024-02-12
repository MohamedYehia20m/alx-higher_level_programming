#!/usr/bin/node

const integerValue = parseInt(process.argv[2]);

if (!isNaN(integerValue)) {
  console.log('My number: ' + integerValue);
} else {
  console.log('Not a number');
}
