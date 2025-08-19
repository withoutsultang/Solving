const fs = require('fs').readFileSync(0, 'utf-8').toString().trim().split(" ").map(Number);

const [a,b,c] = fs;

console.log((a+b)%c);
console.log(((a%c)+(b%c))%c);
console.log((a*b)%c);
console.log(((a%c)*(b%c))%c);