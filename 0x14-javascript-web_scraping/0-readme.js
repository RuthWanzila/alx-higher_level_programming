#!/usr/bin/node

const filePath = process.argv[2];
try {
	const content = fs.readFileSync(filePath, 'utf8');
	console.log(content);
} catch (err) {
	console.log(err);
}
