let questions = [
    "Фамилия:",
    "Имя:",
    "Отчество:",
    "Год рождения:",
    "Город проживания:",
    "Пол (м/ж):",
    "Профессия:",
    "Образование:",
    "Телефон:",
    "Электронная почта:"
];

let answers = [];

for (let i = 0; i < questions.length; i++) {
    let answer = prompt(questions[i]);
    answers.push(answer);
}

let currentYear = new Date().getFullYear();
let birthYear = parseInt(answers[3]);
let age = currentYear - birthYear;

let currentDate = new Date();
let formattedDate = currentDate.toLocaleDateString();
let formattedTime = currentDate.toLocaleTimeString();

function getFioInGenitive(surname, name, patronymic) {
    if (surname.endsWith('а')) {
        genitiveSurname = surname.slice(0, -1) + 'ой';
    } else if (surname.endsWith('ов') || surname.endsWith('ев')) {
        genitiveSurname = surname + 'а';
    } else {
        genitiveSurname = surname + 'а';
    }

    if (name.endsWith('а')) {
        genitiveName = name.slice(0, -1) + 'ы';
    } else {
        genitiveName = name + 'а';
    }

    if (patronymic.endsWith('а')) {
        genitiveLastName = patronymic.slice(0, -1) + 'ы';
    } else {
        genitiveLastName = patronymic + 'а';
    }

    return `${genitiveSurname} ${genitiveName} ${genitiveLastName}`;
}

let fioRodPadezh = getFioInGenitive(answers[0], answers[1], answers[2]);

let tableHTML = `
    <h2>Анкета ${fioRodPadezh}</h2>
    <table>
        <tr><th>Вопрос</th><th>Ответ</th></tr>
`;

for (let i = 0; i < questions.length; i++) {
    tableHTML += ` 
        <tr>
            <td>${questions[i]}</td> 
            <td>${answers[i]}</td> 
        </tr>
    `;
}

tableHTML += ` 
    <tr> 
        <td>Возраст</td> 
        <td>${age} лет</td> 
    </tr> 
    <tr> 
        <td>Дата анкетирования</td> 
        <td>${formattedDate}</td> 
    </tr> 
    <tr> 
        <td>Время анкетирования</td> 
        <td>${formattedTime}</td> 
    </tr> 
</table>`;

document.getElementById('form').innerHTML = tableHTML;