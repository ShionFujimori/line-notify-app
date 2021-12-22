# line-notify-app
LINE Notification App

## Usage
1. Get `.env` file which contains LINE token, and place it under the root directory.
2. Create a empty `images` folder under the root directory.
3. One-time run: `python app.py -type {stock, search-num} -keyword KEYWORD` 
4. Periodic run: `crontab cron.txt` (default: type='stock', keyword='cad jpy')

### How to change the periodic run settings?
1. Open the cron.txt file, and change the settings.
2. `crontab cron.txt`

### How to stop the periodic run?
1. Open the cron.txt, and comment out the settings.
2. `crontab cron.txt`
