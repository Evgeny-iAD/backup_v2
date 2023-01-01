import warnings
from datetime import date, timedelta, datetime
import logging.config


warnings.filterwarnings('ignore', '.*Failed to load HostKeys.*')
current_date = date.today()
user_db = 'root'
secret_db = 'PaSdbR00t'
port = 22
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
logging.basicConfig(filename='Transport.log', level=logging.INFO, filemode='a+')
data_json = {}
Time_limit = 100


# ЗАПУСК ПРОГРАММЫ
if __name__ == '__main__':
    print_hi('PyCharm')

