# line-notify-app
LINE Notification App

## Usage
1. Create a virtual Python environment and install all libraries in requirements.txt
```
virtualenv env
source env/bin/activate

pip install -r requirements.txt
```
2. Get `.env` file which contains LINE token, and place it under the root directory.
3. Create a empty `images` folder under the root directory.
4. One-time run
```
python app.py -type {stock, search-num} -keyword KEYWORD
```
5. Periodic run (default: type='stock', keyword='cad jpy')
```
crontab cron.txt
```

### How to change the periodic run settings?
1. Open the cron.txt file, and change the settings.
2. `crontab cron.txt`

### How to stop the periodic run?
1. Open the cron.txt, and comment out the settings.
2. `crontab cron.txt`

### Aside: How to edit the crontab file directly?
```
crontab -e
```

### Aside: How to view the content of crontab file?
```
crontab -l
```
