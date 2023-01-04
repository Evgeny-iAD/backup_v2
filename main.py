import json
import warnings
from datetime import date, timedelta, datetime
import logging.config
import export_db as ex
import pysftp
import datetime
import time
import  schedule


warnings.filterwarnings('ignore', '.*Failed to load HostKeys.*')
current_date = date.today()
user_db = ''
secret_db = ''
port = 22
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
logging.basicConfig(filename='Transport.log', level=logging.INFO, filemode='a+')
data_json = {}
Time_limit = 100

# Чтение файлка конфигурации json
def read_connect_json(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        print('Файл конфигурации не найден')

def job():
    print("Запускаю процесс...")
    data_json = read_connect_json('connect_path.json')
    obj = json.loads(data_json)
    remotepath = obj['remoteP']
    localpath = obj['localP']
    host_db = obj['host']
    d = date.today()
    export = ex.Export_DB(host_db, user_db, secret_db, cnopts, remotepath, localpath, d)
    export.transport()

# ЗАПУСК ПРОГРАММЫ
if __name__ == '__main__':

    data_json = read_connect_json('connect_path.json')
    obj = json.loads(data_json)
    remotepath = obj['remoteP']
    localpath = obj['localP']
    host_db = obj['host']

    d = date.today()
    # d = '2023-01-03'

    schedule.every().day.at("23:43").do(job)

    # print(f'{export.scan_dump()}')
    # export.scan_dump()
    # export.transport()


    while True:
        schedule.run_pending()
        time.sleep(1)
        # currenttime = time.localtime()
        # timestamp = time.strftime('%H', currenttime)
        # time.sleep(1800)
        # if int(timestamp) >= 4 and int(timestamp) <= 5:
        #     print(f'Время пришло {d}')
        #     export = ex.Export_DB(host_db, user_db, secret_db, cnopts, remotepath, localpath, d)
        #     export.transport()
        #     break

        # if timestamp

