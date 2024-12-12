let x = prompt('Введите x, где 0<x<=10','0')
let res = 1
for (let i = 2; i <= x; i++) {
    res *= i
}
alert('Результат: ' + x + '! = ' + res)