from bs4 import BeautifulSoup
import requests
from pprint import pprint
from app.routes.parse.parse_amindi_org import parse_amindi_org


def parse_amindi_ge(city):
    cities = parse_amindi_org()
    url1 = f'https://amindi.ge/ka/city/{city}/?d=5'
    response = requests.get(url1)
    soup = BeautifulSoup(response.content,'html.parser')
    data = {}
    data_values = []
    data_keys = []
    items = soup.find_all('div', class_='degrees')
    weekdays = soup.find_all('div', class_='weekDay')

    for keys in weekdays:
        data_keys.append(keys.get_text(strip=True))
    for item in items[1:]:
        data_values.append(item.get_text(strip=True))
    for weekday, celsus in zip(data_values, data_keys):
        data[celsus] = weekday

    return data,cities

if __name__ == "__main__":
    pprint(parse_amindi_ge())