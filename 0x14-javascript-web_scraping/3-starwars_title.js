#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const apiURL = 'https://swapi-api.hbtn.io/api/films/';

request(apiURL + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const JSONresp = JSON.parse(body);
    console.log(JSONresp.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
