function calcAns() {
    let a = parseFloat(document.getElementById("a").value);
    let b = parseFloat(document.getElementById("b").value);
    let c = parseFloat(document.getElementById("c").value);
    let d = parseFloat(document.getElementById("d").value);
    let x = parseFloat(document.getElementById("x").value);
    let y = parseFloat(document.getElementById("y").value);

    let result1 = ((b + Math.sqrt(Math.pow(b, 2) + 4 * a * c)) / (2 * a)) - Math.pow(a, 3) * c + Math.pow(b, -2);
    let result2 = Math.sin(x) + Math.cos(y);
    let result3 = Math.log(a) + b * Math.sin(c);
    let result4 = Math.pow(d, 2) - (x * y);

    document.getElementById("result1").textContent = result1.toFixed(2);
    document.getElementById("result2").textContent = result2.toFixed(2);
    document.getElementById("result3").textContent = result3.toFixed(2);
    document.getElementById("result4").textContent = result4.toFixed(2);
}