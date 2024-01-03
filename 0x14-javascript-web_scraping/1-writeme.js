#!/usr/bin/node
const req = require('req');
req.writeFile(process.argv[2], process.argv[3], error => {
	if (error) console.log(error);
});
