from datetime import date, timedelta, datetime
import logging.config
import pysftp

class Export_DB:
    def __init__(self, host, user, secret, cnopts, remotepath, localpath, d):
        self.host = host
        self.user = user
        self.secret = secret
        self.cnopts = cnopts
        self.remotepath = remotepath
        self.localpath = localpath
        self.d = d

    def scan_dump(self):
        try:
            print(self.remotepath)
            print(self.localpath)
            print(self.host)
            with pysftp.Connection(host=self.host, port=22, username=self.user, password=self.secret,
                                   cnopts=self.cnopts) as sftp:
                try:
                    date_dump = []
                    print(self.remotepath)
                    print(f'Соединение установлено в {datetime.now()} ')
                    logging.info('-------------------------------------------------------------------')
                    logging.info(f'Соединение установлено в {datetime.now()} ')
                    sftp.cwd(self.remotepath)
                    dir_struct = sftp.listdir_attr()
                    for attr in dir_struct:
                        if attr.filename.split('.')[0] == 's11':
                            # if attr.filename.split('.')[1] == f'{current_date}':
                            x = attr.filename.split('.')[1]
                            date_dump.append(x)
                            print(f'Бэкап s11 на дату {x} найден')
                        if attr.filename.split('.')[0] == 'mes':
                            # if attr.filename.split('.')[1] == f'{current_date}':
                            # print('Бэкап mes на текущую дату найден')
                            pass
                except:
                    print("ошибка передачи")
                    logging.info("ошибка хоста")
        except:
            print("ошибка хоста")
            logging.info('Ошибка')
            logging.error('Ошибка передачи данных')
        return date_dump

    def transport(self):
        # self.progres_start()
        logging.info('-------------------------------------------------------------------')
        print('Подключение к серверу...')  # 12,5%
        # ui.progressBar.setValue(12)
        try:
            with pysftp.Connection(host=self.host, port=22, username=self.user, password=self.secret,
                                   cnopts=self.cnopts) as sftp:
                print('Подключение к серверу прошло успешно...')  # 25%
                logging.info(f'Подключение к серверу прошло успешно... ')

                print('Начинаю процесс копирования s11...')  # 37,5%
                logging.info('Начинаю процесс копирования s11...')

                sftp.get(
                    Path_file(self.remotepath, 's11', f'{self.d}').__str__(),
                    Path_file(self.localpath, 's11', f'{self.d}').__str__()
                )
                print('Процесс копирования дампа s11 завершен')  # 50%
                logging.info('Процесс копирования дампа s11 завершен')

            with pysftp.Connection(host=self.host, port=22, username=self.user, password=self.secret,
                                   cnopts=self.cnopts, ) as sftp:
                print('Подключение к серверу прошло успешно...')  # 62,5%
                logging.info('Процесс копирования дампа s11 завершен')

                print('Начинаю процесс копирования mes...')  # 75%
                logging.info('Начинаю процесс копирования mes...')

                sftp.get(
                    Path_file(self.remotepath, 'mes', f'{self.d}').__str__(),
                    Path_file(self.localpath, 'mes',  f'{self.d}').__str__()
                )
                print('Процесс копирования дампа mes завершен')  # 87,5%
                logging.info('Процесс копирования дампа mes завершен')

        except:
            print('Дамп БД не найден!')
            logging.info('Дамп БД не найден!')
        print('процедура загрузки дампов завершена')  # 100%
        logging.info('процедура загрузки дампов завершена')


class Path_file:
    def __init__(self, path, db, data):
        self.db = str(db)
        self.data = data
        self.path = str(path)

    def __str__(self):
        print(f'{self.path}{self.db}.{self.data}.sql')
        logging.info(f'{self.path}{self.db}.{self.data}.sql')
        return f'{self.path}{self.db}.{self.data}.sql'
        # if self.path == 'remote':
        #     return f'/home/backup/{self.db}.{self.data}.sql.gz'
        # else:
        #     # slesh = r'\\'
        #     return f"C:\SHARE\{'b'}ackup\{self.db}.{self.data}.sql.gz"
        # \\192.168.0.69\arhiv