#!/usr/bin/node
const i = 0;
exports.logMe = function (item)
{
	console.log(`${i++}: ${item}`);
};
