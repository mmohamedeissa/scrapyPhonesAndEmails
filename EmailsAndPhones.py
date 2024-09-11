import re
import requests
from bs4 import BeautifulSoup


def get_emails_and_phones(website_link):
    try:
        html = requests.get(website_link).text
    except:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    # Regular expression patterns for emails and phone numbers
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'

    # Find all emails and phone numbers
    emails = re.findall(email_pattern, soup.get_text())
    phones = re.findall(phone_pattern, soup.get_text())

    return {'emails': emails, 'phones': phones}


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
    contact_info = get_emails_and_phones(website_link)
    try:
        if contact_info['emails'] or contact_info['phones']:
            return contact_info
    except:
        pass
    links_con = get_content_links(website_link)

    if not links_con:
        return None

    for i in links_con:
        contact_info = get_emails_and_phones(i)

        try:
            if contact_info['emails'] or contact_info['phones']:
                return contact_info
        except:
            pass

    return None


contact_info = main('Website')
print(contact_info)
