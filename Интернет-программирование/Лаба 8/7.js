let x = prompt("Введите двоичное число:");
let res = 0;
let length = x.length;

for (let i = 0; i < length; i++) {
    let bit = x[length - 1 - i];
    res += bit * Math.pow(2, i);
}
alert('В десятичной системе: ' + res);