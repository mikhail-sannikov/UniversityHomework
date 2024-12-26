import requests


def main() -> None:
    try:
        lat = float(input('Широта объекта: '))
        lon = float(input('Долгота объекта: '))
        save_satellite_image((lat, lon))
    except ValueError:
        print('Ошибка ввода! Введите координаты в виде десятичных чисел')


def save_satellite_image(coords: tuple, zoom: int = 16, filename: str = 'media/satellite_image.png') -> None:
    base_url = 'https://static-maps.yandex.ru/1.x/'
    params = {'ll': f'{coords[1]},{coords[0]}', 'z': zoom, 'l': 'sat', 'size': '600,400'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Снимок сохранён в файл {filename}')
    else:
        print(f'Не удалось получить снимок: {response.status_code}')
        print('Ответ сервера:', response.text)


if __name__ == '__main__':
    main()
