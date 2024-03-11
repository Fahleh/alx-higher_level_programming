#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);

const factorial = (n) => {
  return n === 0 || isNaN(n)? 1 : n * factorial(n - 1);
}

console.log(factorial(num));
