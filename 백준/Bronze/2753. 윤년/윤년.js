const fs = require('fs').readFileSync(0, 'utf-8').toString().trim();
const year = Number(fs);

if( (year%4===0) && (year%100!==0 | year%400===0) ){
    console.log(1);
} else console.log(0);