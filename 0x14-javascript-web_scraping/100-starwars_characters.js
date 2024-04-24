#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const xters = data.characters;
  for (const item of xters) {
    request.get(item, function (error, res, newBody) {
      if (error) {
        console.log(error);
      }
      const newData = JSON.parse(newBody);
      console.log(newData.name);
    });
  }
});
