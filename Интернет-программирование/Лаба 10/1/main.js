document.getElementById('ps').addEventListener('change', handleSelection);

function handleSelection() {
    const selectValue = document.getElementById('ps').value;
    document.getElementById('ps_photo_area').innerHTML = `<img src="${selectValue}" alt="картинка">`
}