#!/usr/bin/node
const args = process.argv;
const isInteger = parseInt(args[2]);

if (isNaN(isInteger))
	console.log('Not a number');
else
	console.log('My number: ', isInteger);
