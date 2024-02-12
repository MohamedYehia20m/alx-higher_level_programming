#!/usr/bin/node

const { argv } = require('node:process');
let counter = argv.length;

(counter === 2) ? console.log('No argument') : console.log('Argument found');
