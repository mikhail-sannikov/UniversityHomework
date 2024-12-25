document.getElementById('send_btn').addEventListener('click', function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });
});

function getFioInGenitive(surname, name, patronymic) {
    let genitiveSurname, genitiveName, genitiveLastName;

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

function submitForm() {
    let form = document.getElementById('student_form');
    let [surname, name, patronymic] = form.fio.value.split(' ');
    let birthYear = parseInt(form.birthYear.value);
    let gender = form.gender.value;
    let faculty = form.faculty.value;
    let specialty = form.specialty.value;
    let course = form.course.value;
    let hobbies = form.hobbies.value;
    let languages = Array.from(form.querySelectorAll('input[name="languages"]:checked')).map(el => el.value).join(', ');
    let instruments = Array.from(form.querySelectorAll('input[name="instruments"]:checked')).map(el => el.value).join(', ');
    let sports = form.sports.value;
    let color = form.color.value;

    let currentYear = new Date().getFullYear();
    let age = currentYear - birthYear;
    let currentDate = new Date();

    let fioInGenitive = getFioInGenitive(surname, name, patronymic);
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2 id="fio_in_genetive">Анкета ${fioInGenitive}</h2>
        <table>
            <tr><th>ФИО</th><td>${surname} ${name} ${patronymic}</td></tr>
            <tr><th>Возраст</th><td>${age}</td></tr>
            <tr><th>Пол</th><td>${gender}</td></tr>
            <tr><th>Факультет</th><td>${faculty}</td></tr>
            <tr><th>Специальность</th><td>${specialty}</td></tr>
            <tr><th>Курс</th><td>${course}</td></tr>
            <tr><th>Хобби</th><td>${hobbies}</td></tr>
            <tr><th>Языки</th><td>${languages}</td></tr>
            <tr><th>Музыкальные инструменты</th><td>${instruments}</td></tr>
            <tr><th>Любимые виды спорта</th><td>${sports}</td></tr>
            <tr><th>Любимый цвет</th><td><span style="background-color:${color}; color:white; padding:3px 10px;">${color}</span></td></tr>
            <tr><th>Дата и время анкетирования</th><td>${currentDate.toLocaleString()}</td></tr>
        </table>
    `;
}