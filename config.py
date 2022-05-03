import yaml
import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG_FILE_PATH = os.path.join(ROOT_PATH, 'env.yaml')

if os.path.exists(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, 'r') as file:
        data = yaml.safe_load(file)
else:
    data = dict()

SECRET_KEY = data.get('SECRET_KEY', 'secret_key')

LOG_FILE = data.get('LOG_FILE', os.path.join(ROOT_PATH, 'tmp/output.log'))

SQLALCHEMY_DATABASE_URI = data.get('SQLALCHEMY_DATABASE_URI',
                                   'sqlite:///' + os.path.join(ROOT_PATH, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SMTP = data.get('SMTP', dict(
    app_name='',
    email='',
    password='',
    host='',
    port=''
))

POSTS_PER_PAGE = 3

LANGUAGES = ['en', 'vi']

MS_TRANSLATOR_KEY = data.get('MS_TRANSLATOR_KEY')


class SMTP():
    app_name = SMTP['app_name']
    email = SMTP['email']
    password = SMTP['password']
    host = SMTP['host']
    port = SMTP['port']


ELASTIC_SEARCH = data.get('ELASTIC_SEARCH', dict(
    host='',
    username='',
    password=''
))


class ELASTIC_SEARCH():
    host = ELASTIC_SEARCH['host']
    username = ELASTIC_SEARCH['username']
    password = ELASTIC_SEARCH['password']