import requests


def show_stadiums_map() -> None:
    stadiums_location = {
        'Лужники': '37.554191,55.715551',
        'Спартак': '37.440262,55.818015',
        'Динамо': '37.559809,55.791540',
    }

    markers = '~'.join([f'{coords},pm2rdm' for coords in stadiums_location.values()])
    map_url = 'https://static-maps.yandex.ru/1.x/'
    params = {'l': 'map', 'size': '600,400', 'pt': markers}

    response = requests.get(map_url, params=params)

    if response.status_code == 200:
        html_content = f'<html><body><img src="{response.url}" alt="карта"></body></html>'
        with open('media/stadiums_map.html', 'w') as file:
            file.write(html_content)
        print("Карта сохранена в файле 'stadiums_map.html'")
    else:
        print('Ошибка при загрузке карты')


if __name__ == '__main__':
    show_stadiums_map()
