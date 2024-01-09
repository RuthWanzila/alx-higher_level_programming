#!/usr/bin/node
let Items = 0;

exports.logMe = function (item) {
  console.log(`${Items}: ${item}`);
  Items++;
};
