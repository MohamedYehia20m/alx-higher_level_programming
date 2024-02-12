#!/usr/bin/node

const { argv } = require('node:process');
let counter = 0;

argv.forEach((val, index) => {
  counter += 1;
});
(counter === 2) ? console.log('No argument') : console.log('Argument found');
