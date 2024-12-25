const errorMsg = document.querySelector('.form__error-msg');
const successMsg = document.querySelector('.form__success-msg');

const form = document.querySelector('.form');
const fields = form.querySelectorAll('form input');

const name = form.querySelector('#profile-name');
const age = form.querySelector('#profile-age');
const phone = form.querySelector('#profile-phone');
const love_number = form.querySelector('#profile-number');

let k = 0;

form.addEventListener('submit', function (event) {
    event.preventDefault()

    removeError()

    // обработка ошибок
    letters(name)
    ages(age)
    phones(phone)
    numbers(love_number)
    // конец обработки ошибок

    success(k)
})

const genError = function (text) {
    let error = document.createElement('div')

    error.classList.add('error')
    error.style.color = 'red'
    error.style.fontSize = '12px'
    error.innerHTML = text

    return error
};

const removeError = function () {
    let errors = form.querySelectorAll('.error')
    k = 0

    for (var i = 0; i < errors.length; i++) {
        errorMsg.style.display = 'none'
        successMsg.style.display = 'block'
        errors[i].remove()
    }
    for (var i = 0; i < fields.length; i++) {
        fields[i].classList.remove('input_error')
    }
};

const letters = function (input) {
    if (input.dataset.validator === 'letters') {
        if (input.value) {
            if (/^[a-zа-яё]+$/i.test(input.value.trim())) {
                k += 1
            }
            else {
                input.classList.add('input_error')
                let error = genError('Только Русские или Английские буквы!')
                input.parentElement.insertBefore(error, input)
            }
        }
        else {
            input.classList.add('input_error')
            let error = genError('Поле не заполнено')
            input.parentElement.insertBefore(error, input)
        }
    }
};

const ages = function (input) {
    const error_message = 'Число от 0 до 100!!!'

    if (input.dataset.validator === 'number') {
        if (/^[0-9]+$/.test(input.value.trim())) {
            if ((parseInt(input.value) > parseInt(input.dataset.validatorMin)) && (parseInt(input.value) < parseInt(input.dataset.validatorMax))) {
                k += 1
            }
            else {
                let error = genError(error_message)

                input.parentElement.insertBefore(error, input)
                input.classList.add('input_error')
            }
        }
        else {
            let error = genError(error_message)

            input.parentElement.insertBefore(error, input)
            input.classList.add('input_error')
        }
    }
};

const phones = function (input) {
    if (input.dataset.validator === 'regexp') {
        if (/^\+7\d{10}$/.test(input.value.trim())) {
            k += 1
        }
        else {
            let error = genError('Неверный формат!')

            input.parentElement.insertBefore(error, input)
            input.classList.add('input_error')
        }
    }
};

const numbers = function (input) {
    if (input.dataset.validator === 'number') {
        if (/^[0-9]+$/.test(input.value.trim())) {
            k += 1
        }
        else {
            let error = genError('Это не число!')

            input.parentElement.insertBefore(error, input)
            input.classList.add('input_error')
        }
    }
};

const success = function (k) {
    if (k === 4) {
        errorMsg.style.display = 'none'
        successMsg.style.display = 'block'
    }
    else {
        errorMsg.style.display = 'block'
        successMsg.style.display = 'none'
    }
};

name.onblur = function() {
    if (name.value) {
        console.log(`Проверка введенного имени -> ${name.value}`)
        letters(name)
    }
}
name.onfocus = function() {
    let error = form.querySelector('.error')
    if (error)
        error.remove()
    name.classList.remove('input_error')
}

age.onblur = function() {
    if (age.value) {
        console.log(`Проверка введенного возраста -> ${age.value}`)
        ages(age)
    }
}
age.onfocus = function() {
    let error = form.querySelector('.error')
    if (error)
        error.remove()
    age.classList.remove('input_error')
}

phone.onblur = function() {
    if (phone.value) {
        console.log(`Проверка введенного телефона -> ${phone.value}`)
        phones(phone)
    }
}
phone.onfocus = function() {
    let error = form.querySelector('.error')
    if (error)
        error.remove()
    phone.classList.remove('input_error')
}

love_number.onblur = function() {
    if (love_number.value) {
        console.log(`Проверка введенного любимого числа -> ${love_number.value}`)
        numbers(love_number)
    }
}
love_number.onfocus = function() {
    let error = form.querySelector('.error')
    if (error)
        error.remove()
    love_number.classList.remove('input_error')
}