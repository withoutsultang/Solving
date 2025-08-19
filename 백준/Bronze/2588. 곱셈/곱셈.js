const fs = require('fs').readFileSync(0, 'utf-8').toString().trim().split("\n");
const second = fs[1].split("");

for(let i=2; i>=0; i--){
    console.log(fs[0] * second[i]);
}

console.log(fs[0]*fs[1]);