#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);

const printSquare = () => {
        if (isNaN(size))
                console.log('Missing size');
        else {
        let i = 0;
        while (i < size) {
                console.log('X'.repeat(size));
                i++;
        }
        }
}

printSquare();
