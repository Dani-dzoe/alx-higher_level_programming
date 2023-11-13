#!/usr/bin/node

let m = process.argv;
if (m[2] === 'undefined')
{
	console.log('No argument');
}
else
{
	console.log(m[2]);
}
