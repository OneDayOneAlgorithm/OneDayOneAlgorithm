const fs = require('fs');
const arr = fs.readFileSync(0,'utf8').toString().split(' ');
const A = parseInt(arr[0]);
const B = parseInt(arr[1]);
console.log(A+B);