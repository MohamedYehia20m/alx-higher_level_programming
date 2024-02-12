#!/usr/bin/node
function factorial (a) {
  let val;
  try {
    val = parseInt(a);
  } catch (RangeError) {
    console.log('Infinity');
  }
  if ((val === 0) || (val === 1) || (isNaN(val))) { return 1; }
  return parseInt(val) * factorial(val - 1);
}

console.log(factorial(process.argv[2]));
