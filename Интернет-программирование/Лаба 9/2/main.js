function calcLength(point1, point2) {
    return Math.sqrt(Math.pow(point2.x - point1.x, 2) + Math.pow(point2.y - point1.y, 2));
}

function calcSides(A, B, C) {
    let AB = calcLength(A, B);
    let BC = calcLength(B, C);
    let CA = calcLength(C, A);
    return { AB, BC, CA };
}

function calcP(sides) {
    return sides.AB + sides.BC + sides.CA;
}

function calcS(sides) {
    let s = (sides.AB + sides.BC + sides.CA) / 2;
    return Math.sqrt(s * (s - sides.AB) * (s - sides.BC) * (s - sides.CA));
}

document.getElementById('calculateButton').addEventListener('click', function() {
    let A = { x: parseFloat(document.getElementById('ax').value), y: parseFloat(document.getElementById('ay').value) };
    let B = { x: parseFloat(document.getElementById('bx').value), y: parseFloat(document.getElementById('by').value) };
    let C = { x: parseFloat(document.getElementById('cx').value), y: parseFloat(document.getElementById('cy').value) };

    let sides = calcSides(A, B, C);
    let P = calcP(sides);
    let S = calcS(sides);

    document.getElementById('results').innerHTML =
        '<p>Длины сторон треугольника:</p>' +
            'AB: ' + sides.AB.toFixed(2) +
            '<br>BC: ' + sides.BC.toFixed(2) +
            '<br>CA: ' + sides.CA.toFixed(2) +
        '<p>Периметр треугольника: ' + P.toFixed(2) + '<br>' +
        'Площадь треугольника: ' + S.toFixed(2) + '</p>';
});