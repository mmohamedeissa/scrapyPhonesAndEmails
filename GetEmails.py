# BY Mohamed Eissa

import re

import requests
from bs4 import BeautifulSoup


def get_emails(website_link):

    try:
        html = requests.get(website_link).text
    except:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = []
    emails = re.findall(email_pattern, soup.get_text())

    if not emails:
        emails = []
    return emails


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
    emails = get_emails(website_link)
    links_con = []
    if len(emails) == 0:
        links_con = get_content_links(website_link)
    else:
        return emails[0]


    if len(links_con) == 0 :
        return None


    for i in links_con:
        emails = get_emails(i)

        if len(emails) != 0:
            return emails[0]

    return None


email = main('WebsiteLink')

print(email)
