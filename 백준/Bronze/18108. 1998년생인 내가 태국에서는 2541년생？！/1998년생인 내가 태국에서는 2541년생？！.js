const fs = require('fs').readFileSync(0, 'utf-8').toString().trim();

if(fs >= 1000 && fs <= 3000){
    console.log(Number(fs)-543);
} else {
    return;
}