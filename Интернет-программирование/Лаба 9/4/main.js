let userInput = prompt("Введите через пробел двадцать слов:");
let words = userInput.split(' ');

let glasn = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ю', 'я'];

function isGlasn(word) {
    let firstLetter = word[0].toLowerCase();
    return glasn.indexOf(firstLetter) !== -1;
}

function highlightWords(list) {
    let result = '';
    for (let i = 0; i < list.length; i++) {
        if (isGlasn(list[i])) {
            result += '<span class="glasn">' + list[i] + '</span>';
        } else {
            result += list[i];
        }
        if (i < list.length - 1) {
            result += ', ';
        }
    }
    return result;
}

let soglWords = [];

for (let i = 0; i < words.length; i++) {
    if (!isGlasn(words[i])) {
        soglWords.push(words[i]);
    }
}

document.getElementById('original').innerHTML = highlightWords(words);
document.getElementById('reversed').innerHTML = highlightWords(words.slice().reverse());
document.getElementById('sorted').innerHTML = highlightWords(words.slice().sort());
document.getElementById('sogl').innerHTML = soglWords.join(', ');