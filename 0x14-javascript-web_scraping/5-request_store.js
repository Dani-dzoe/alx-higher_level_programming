#!/usr/bin/node

const req = require('req');
const request = require('request');
request(process.argv[2]).pipe(req.createWriteStream(process.argv[3]));
