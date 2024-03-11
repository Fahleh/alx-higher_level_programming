#!/usr/bin/node
const args = process.argv;
const n = parseInt(args[2]);

const factorial = (num) => {
	return num === 0 || isNaN(num)? 1 : num * factorial(num - 1);
}

console.log(factorial(n));
