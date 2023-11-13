#!/usr/bin/node

let myArg = process.argv;
console.log(typeof myArg[2] === 'undefined' ? 'No argument' : myArg[2]);
