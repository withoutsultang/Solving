const fs = require('fs').readFileSync(0, 'utf-8').toString().trim().split('\n');
const repeat = Number(fs[0]);

for(let i=1; i<fs.length; i++){
    const [a,b] = fs[i].split(" ").map(Number);
    
    console.log(a+b);
}