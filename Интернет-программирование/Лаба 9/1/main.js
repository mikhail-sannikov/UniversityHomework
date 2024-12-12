function main() {
    const a = parseFloat(document.getElementById('numA').value);
    const b = parseFloat(document.getElementById('numB').value);
    const c = parseFloat(document.getElementById('numC').value);

    if (isNaN(a) || isNaN(b) || isNaN(c)) {
        document.getElementById('result').innerText = "Введите все три числа!";
        return;
    }

    document.getElementById('result').innerText = `Наименьшее число: ${findSmallest(a, b, c)}`;
}

function findSmallest(a, b, c) {
    let smallest = a;

    for (const num of [b, c]) {
        if (num < smallest) {
            smallest = num
        }
    }

    return smallest;
}