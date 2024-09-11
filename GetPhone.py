import re

import requests
from bs4 import BeautifulSoup


def get_phones(website_link):

    try:
        html = requests.get(website_link).text
    except:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    phone_pattern = r'\+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
    phones = re.findall(phone_pattern, soup.get_text())
    phones = [i for i in phones if len(i) >= 9]

    if not phones:
        phones = []
    return phones


def get_content_links(website_link):
    try:
        html = requests.get(website_link).text
    except:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.find_all('a')

    content_urls = []

    for i in all_links:
        try:
            if 'contact' in i['href']:
                content_urls.append(i['href'])
        except:
            pass
    return content_urls


def main(website_link):
    phones = get_phones(website_link)

    links_con = []
    try:
        if len(phones) == 0:
            links_con = get_content_links(website_link)
        else:
            return phones[0]
    except:
        pass

    if len(links_con) == 0:
        return None

    for i in links_con:
        try:
            phones = get_phones(i)

            if len(phones) != 0:
                return phones[0]
        except:
            pass
    return None


phone = main('WebsiteLink')