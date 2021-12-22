import requests
import os
import time
import datetime
import urllib
from dotenv import load_dotenv

# web crawling
from selenium import webdriver
from selenium.webdriver.common.by import By

# web scraping
from bs4 import BeautifulSoup


# Obtain LINE token from .env file
load_dotenv()
LINE_TOKEN = os.getenv('LINE_TOKEN')

# API URL
API_URL = 'https://notify-api.line.me/api/notify'

def send_notification(message: str):
    """ Send LINE notification
    """
    dt_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    token_dict = {'Authorization': f'Bearer {LINE_TOKEN}'}
    send_dict = {'message': dt_now + '\n' + message}

    post = requests.post(API_URL, headers=token_dict, data=send_dict)

    if post.status_code == 200:
        print(f'{dt_now}: Successful')
    else:
        print(f'{dt_now}: Error')


def get_message():
    """
    """
    message = \
    """\n
    123
    456
    """
    return message


def get_search_results_num(search_words: str, window=False):
    """ Get a number of search results for `search_words`.

    Args:
        - window: if True, then a window browser will be opened.
    """
    # Initialize Google Chrome
    # (Need to install ChromeDriver: `brew install chromedriver`)
    global browser
    if not window:
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        browser = webdriver.Chrome(options=op)
    else:
        browser = webdriver.Chrome()

    # Go to google.com
    browser.get('https://www.google.com/')
    time.sleep(2)

    # Type in `search_words` into the textbox
    elem = browser.find_element(By.NAME, 'q')
    elem.clear()
    elem.send_keys(search_words)
    time.sleep(2)
    
    # Click search button
    button = browser.find_element(By.NAME, 'btnK')
    button.click()

    # Extract a number of search results
    result = browser.find_element(By.ID, 'result-stats').text

    return f'"{search_words}": {result}'




if __name__ == '__main__':
    message = get_search_results_num('aaa')
    # message = get_message()

    send_notification(message)
