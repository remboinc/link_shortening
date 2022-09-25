import re
import requests
import os
from dotenv import load_dotenv


def shorten_link(bitlink_token, user_link):
    long_url = {'long_url': user_link}
    header = {'Authorization': f'Bearer {bitlink_token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=header, json=long_url)
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink


def count_clicks(bitlink_token, user_link):
    header = {'Authorization': f'Bearer {bitlink_token}'}
    bitlink = re.sub(r'https://', '', user_link)
    count_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(count_clicks_url, headers=header)
    response.raise_for_status()
    total_clicks = response.json().get('total_clicks')
    return total_clicks


def is_bitlink(bitlink_token, user_link):
    header = {'Authorization': f'Bearer {bitlink_token}'}
    bitlink = re.sub(r'https://', '', user_link)
    this_is_bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(this_is_bitlink, headers=header)
    return response.ok


def main():
    load_dotenv()
    user_link = input('Введите url: ')
    bitlink_token = os.getenv('BITLINK_TOKEN')

    try:
        if is_bitlink(bitlink_token, user_link):
            clicks_count = count_clicks(bitlink_token, user_link)
            print(f'По ссылке переходили {clicks_count} раз')
        else:
            bitlink = shorten_link(bitlink_token, user_link)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
