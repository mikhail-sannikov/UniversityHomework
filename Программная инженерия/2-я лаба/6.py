import random
from io import BytesIO
from typing import ByteString

import requests
from PIL import Image


def main() -> None:
    cities = [
        {'name': 'Москва', 'coords': [55.7558, 37.6173]},
        {'name': 'Париж', 'coords': [48.8566, 2.3522]},
        {'name': 'Нью-Йорк', 'coords': [40.7128, -74.0060]},
        {'name': 'Токио', 'coords': [35.6895, 139.6917]},
    ]

    city = random.choice(cities)
    zoom = random.randint(13, 15)
    map_type = random.choice(['sat', 'map'])

    if image_data := get_city_map_yandex(city, zoom, map_type):
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print('Ошибка при получении изображения')


def get_city_map_yandex(city: list, zoom: int, map_type: str) -> ByteString:
    base_url = 'https://static-maps.yandex.ru/1.x/'
    params = {'ll': f"{city['coords'][1]},{city['coords'][0]}", 'z': zoom, 'size': '600,400', 'l': map_type}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.content
    else:
        print('Не удалось загрузить карту.')
        return None


if __name__ == '__main__':
    main()
