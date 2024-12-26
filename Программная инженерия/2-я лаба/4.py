import os
from typing import Optional

import requests
from dotenv import load_dotenv


def main() -> None:
    api_key = os.getenv('YANDEX_API_TOKEN')
    cities = input('Введите список городов через запятую: ').split(',')

    southernmost_city = find_southernmost_city_yandex(cities, api_key)

    if southernmost_city:
        print(f'Самый южный город: {southernmost_city}')
    else:
        print('Не удалось определить самый южный город')


def find_southernmost_city_yandex(city_list: list, api_key: str) -> Optional[str]:
    base_url = 'https://geocode-maps.yandex.ru/1.x/'
    cities_coords = {}

    for city in city_list:
        try:
            params = {'apikey': api_key, 'geocode': city.strip(), 'format': 'json'}
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                geo_data = response.json()
                try:
                    pos = geo_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                    _, lat = map(float, pos.split())
                    cities_coords[city.strip()] = lat
                except (IndexError, KeyError):
                    print(f'Не удалось найти координаты города: {city}')
            else:
                print(f'Ошибка при запросе геокодера для города {city}: {response.status_code}')
        except Exception as e:
            print(f'Ошибка при обработке города {city}: {e}')

    if cities_coords:
        southernmost_city = min(cities_coords, key=cities_coords.get)
        return southernmost_city
    else:
        print('Не удалось обработать ни один из городов.')
        return None


if __name__ == '__main__':
    load_dotenv()
    main()
