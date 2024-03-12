#!/usr/bin/node
const { readFileSync, writeFile } = require('fs');
const args = process.argv;

const getFile = (f) => {
  return readFileSync(f, 'utf8');
};

const temp = getFile(args[2]) + '' + getFile(args[3]);

writeFile(args[4], temp, 'utf8', err => {
  if (err) throw err;
});
