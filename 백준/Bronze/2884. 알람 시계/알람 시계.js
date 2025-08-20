const fs = require('fs').readFileSync(0, 'utf-8').toString().trim().split(" ").map(Number);

let [hour, min] = fs;


if(min - 45 < 0){
    if(hour === 0){
        hour = 24;
    }
    --hour;
    min = 60 - 45 + min;
} else min -= 45;

console.log(`${hour} ${min}`);