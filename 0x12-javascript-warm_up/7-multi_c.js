#!/usr/bin/node

const integerValue = parseInt(process.argv[2]);

if (!isNaN(integerValue)) {
  for (let i = 0; i < integerValue; i++) { console.log('C is fun'); }
} else { console.log('Missing number of occurrences'); }
