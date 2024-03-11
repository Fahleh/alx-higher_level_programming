#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

const add = (a, b) => console.log(a + b);

add(a, b);
