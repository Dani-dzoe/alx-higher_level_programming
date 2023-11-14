#!/usr/bin/node

exports.nh0ccurences = function (list, searchElement)
{
	return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
