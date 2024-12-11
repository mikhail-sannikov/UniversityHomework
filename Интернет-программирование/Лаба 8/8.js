let x = prompt("Введите шестнадцатеричное число:");
let res = 0;
let length = x.length;

for (let i = 0; i < length; i++) {
    let curChar = x[length - 1 - i];
    let curValue;
    if (curChar >= '0' && curChar <= '9') {
        curValue = parseInt(curChar);
    } else if (curChar === 'A') {
        curValue =  10;
    } else if (curChar === 'B') {
        curValue =  11;
    } else if (curChar === 'C') {
        curValue =  12;
    } else if (curChar === 'D') {
        curValue =  13;
    } else if (curChar === 'E') {
        curValue =  14;
    } else if (curChar === 'F') {
        curValue =  15;
    }
    res += curValue * Math.pow(16, i);
}
alert('В десятичной системе: ' + res);