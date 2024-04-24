#!/usr/bin/node

const request = require('request');
const file = process.argv[2];

request.get(file).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
