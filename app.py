import requests
import os
import datetime
from dotenv import load_dotenv


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
    send_dict = {'message': dt_now + message}

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


if __name__ == '__main__':
    message = get_message()
    send_notification(message)
