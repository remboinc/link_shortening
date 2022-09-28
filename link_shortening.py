import re
import requests
import os
from dotenv import load_dotenv
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', nargs='?', default='https://jenyay.net/Programming/Argparse')
    return parser


def shorten_link(bitly_token, user_link):
    long_url = {'long_url': user_link}
    header = {'Authorization': f'Bearer {bitly_token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=header, json=long_url)
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink


def count_clicks(bitly_token, user_link):
    header = {'Authorization': f'Bearer {bitly_token}'}
    bitlink = re.sub(r'https://', '', user_link)
    count_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(count_clicks_url, headers=header)
    response.raise_for_status()
    total_clicks = response.json().get('total_clicks')
    return total_clicks


def is_bitlink(bitly_token, user_link):
    header = {'Authorization': f'Bearer {bitly_token}'}
    bitlink = re.sub(r'https://', '', user_link)
    this_is_bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(this_is_bitlink, headers=header)
    return response.ok


def main():
    load_dotenv()

    parser = createParser()
    urlparse = parser.parse_args()
    user_link = format(urlparse.url)

    bitly_token = os.getenv('BITLY_TOKEN')

    try:
        if is_bitlink(bitly_token, user_link):
            clicks_count = count_clicks(bitly_token, user_link)
            print(f'По ссылке переходили {clicks_count} раз')
        else:
            bitlink = shorten_link(bitly_token, user_link)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print('Неверный ввод')


if __name__ == '__main__':
    main()
