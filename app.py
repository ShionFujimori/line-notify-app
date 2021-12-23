import requests
import os
import time
import datetime
import argparse
from dotenv import load_dotenv

# web crawling & scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Obtain LINE token from .env file
load_dotenv()
LINE_TOKEN = os.getenv('LINE_TOKEN')

# API URL
API_URL = 'https://notify-api.line.me/api/notify'

# Directory path
dir_path = os.path.dirname(os.path.abspath(__file__))


def send_notification(message: str, image=False):
    """ Send LINE notification
    """
    dt_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    token_dict = {'Authorization': f'Bearer {LINE_TOKEN}'}
    send_dict = {'message': dt_now + '\n' + message}

    if image:
        img_dict = {'imageFile': open(os.path.join(dir_path, 'images/stock.png'), mode='rb')}
    else:
        img_dict = {}

    post = requests.post(API_URL, headers=token_dict, data=send_dict, files=img_dict)

    if post.status_code == 200:
        print(f'{dt_now}: Successful')
    else:
        print(f'{dt_now}: Error')


def get_stock(name: str, window=False) -> str:
    """ Get a stock information for `name`

    Args:
        - name: a stock name or keyword.
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

    # Go to Google Finance top page
    browser.get('https://www.google.com/finance/')
    time.sleep(5)

    # Type in `name` into the textbox
    elem = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]')
    elem.clear()
    elem.send_keys(name)
    time.sleep(5)

    # Press enter key
    elem.send_keys(Keys.ENTER)
    time.sleep(5)

    # Get current stock information as an image
    browser.save_screenshot(os.path.join(dir_path, 'images/stock.png'))

    # Quit browser
    browser.quit()

    return f'Stock info: "{name}"'


def get_search_results_num(search_words: str, window=False) -> str:
    """ Get a number of search results for `search_words`.

    Args:
        - search_words: a keyword which will be typed into into a search bar.
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
    
    # Press enter key
    elem.send_keys(Keys.ENTER)

    # Extract a number of search results
    result = browser.find_element(By.ID, 'result-stats').text

    # Quit browser
    browser.quit()

    return f'"{search_words}": {result}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser('This program will send a notification to LINE.')
    parser.add_argument('-type', required=True, choices=['stock', 'search-num'], help='A type of notification')
    parser.add_argument('-keyword', required=True, help='keyword')

    args = parser.parse_args()

    if args.type == 'stock':
        message = get_stock(args.keyword)
        send_notification(message, image=True)
    elif args.type == 'search-num':
        message = get_search_results_num(args.keyword)
        send_notification(message)
