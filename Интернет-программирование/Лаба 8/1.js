let dayInRus = prompt("Введите день недели на русском: ");
let dayInEng;
switch (dayInRus.toLowerCase()) {
    case 'понедельник':
        dayInEng = 'Monday';
        break;
    case 'вторник':
        dayInEng = 'Tuesday';
        break;
    case 'среда':
        dayInEng = 'Wednesday';
        break;
    case 'четверг':
        dayInEng = 'Thursday';
        break;
    case 'пятница':
        dayInEng = 'Friday';
        break;
    case 'суббота':
        dayInEng = 'Saturday';
        break;
    case 'воскресенье':
        dayInEng = 'Sunday';
        break;
    default:
        dayInEng = 'Некорректный ввод. Пожалуйста, введите день недели на русском.';
}
alert(dayInEng);