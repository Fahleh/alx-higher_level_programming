#!/usr/bin/node
const args = process.argv;
const occurrence = parseInt(args[2]);

const printMultiple = () => {
  if (isNaN(occurrence)) {
    console.log('Missing number of occurrences');
  } else {
    let i = 0;
    while (i < occurrence) {
      console.log('C is fun');
      i++;
    }
  }
};

printMultiple();
