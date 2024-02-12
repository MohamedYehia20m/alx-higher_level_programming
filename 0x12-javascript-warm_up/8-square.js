#!/usr/bin/node

const integerValue = parseInt(process.argv[2]);

if (!isNaN(integerValue)) {
  for (let i = 0; i < integerValue; i++) {
    let row = '';
    for (let i = 0; i < integerValue; i++) {
      row += 'X';
    }
    console.log(row);
  }
} else { console.log('Missing size'); }
