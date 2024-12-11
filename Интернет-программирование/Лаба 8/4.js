let x = prompt('Введите трехзначное число:','0')
let sum = 0
while (x > 0) {
    let digit = x % 10
    sum += digit
    x = Math.floor(x / 10)
}
alert('Сумма цифр трехзначного числа: ' + sum);