from bs4 import BeautifulSoup
import requests
from pprint import pprint


def parsed_data_for_api(city):
    api_data = {}

    url = f'https://amindi.ge/ka/city/{city}/?d=5'
    re = requests.get(url)
    parser = BeautifulSoup(re.content, 'html.parser')
    weather_html = parser.find(class_='weather-days-right').find_all(class_='col px-0')

    image_weather_map = {
        '/static/img/weather_small_01.png': 'მზიანი',
        '/static/img/weather_small_02.png': 'ნაწილობრივ ღრუბლიანი',
        '/static/img/weather_small_03.png': 'ღრუბლიანი',
        '/static/img/weather_small_04.png': 'ღრუბლიანი',
        '/static/img/weather_small_06.png': 'უმეტესად ღრუბლიანი',
        '/static/img/weather_small_07.png': 'უმეტესად ღრუბლიანი',
        '/static/img/weather_small_08.png': 'უმეტესად ღრუბლიანი',
        '/static/img/weather_small_14.png': 'ღრუბლიანი',
        '/static/img/weather_small_12.png': 'წვიმიანი',
        '/static/img/weather_small_13.png': 'ნახევრად-წვიმიანი',
        '/static/img/weather_small_18.png': 'წვიმა ჭექა-ქუხილით',
        '/static/img/weather_small_32.png': 'ქარი'

    }

    for weather in weather_html:
        weather_temperature = weather.find_all('span')
        temperature = f'{weather_temperature[0].text}°{weather_temperature[1].text}'
        weekday = weather.find(class_='weekDay').text
        weather_conditions = weather.find('img')['src']
        day = weather.find(class_='day').text

        api_data[weekday] = {'city': city, 'degrees': temperature, 'weather': image_weather_map[weather_conditions],
                             'img': weather_conditions, 'day': day}

    return api_data


if __name__ == '__main__':
    pprint(parsed_data_for_api())
