import os

import requests
from dotenv import load_dotenv


def main() -> None:
    address = input('Введите адрес: ')
    find_district_yandex(address)


def find_district_yandex(address: str) -> None:
    api_key = os.getenv('YANDEX_API_TOKEN')
    geocoder_url = 'https://geocode-maps.yandex.ru/1.x/'
    geocoder_params = {'apikey': api_key, 'geocode': address, 'format': 'json', 'kind': 'district'}

    response = requests.get(geocoder_url, params=geocoder_params)

    if response.status_code == 200:
        geo_data = response.json()
        try:
            district = geo_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData'
            ]['text']
            print(f'Район: {district}')
        except IndexError:
            print('Район не найден.')
    else:
        print('Ошибка при запросе геокодера')


if __name__ == '__main__':
    load_dotenv()
    main()
