const fs = require('fs').readFileSync(0, 'utf-8').toString().trim();
const num = Number(fs);

if(fs>=90){
    console.log('A');
} else if(fs>=80){
    console.log('B');
} else if(fs>=70){
    console.log('C');
} else if(fs>=60){
    console.log('D');
} else console.log('F');