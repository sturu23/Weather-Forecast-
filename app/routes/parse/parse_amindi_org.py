from bs4 import BeautifulSoup
import requests
from pprint import pprint





def parse_amindi_org():
    url = 'https://amindi.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    cities = soup.find('ul', class_='row')
    data_cities = []

    for child in cities.children:
        data_cities.append(child.text.rstrip('\n'))

    while '' in data_cities:
        data_cities.remove('')

    return data_cities

if __name__ == '__main__':
    pprint(parse_amindi_org())