#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.arg[2], process.argv[3], err => {
	        if (err) {
			                console.log(err);
			        }
});
