function handleCalculateBtn() {
    const angleInput = document.getElementById('angle_input')
    const angle = parseFloat(angleInput.value);
    const funcSelect = document.getElementById('function_selector');
    const selectedFunction = funcSelect.value;
    const radians = angle * (Math.PI / 180);

    const expression = 'Math.' + selectedFunction + '(' + radians + ')';
    const result = eval(expression);

    document.getElementById('calculate_result').innerHTML = `<span>Результат: ${result.toFixed(2)}</span>`;
}