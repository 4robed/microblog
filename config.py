import yaml
import os


ROOT_PATH = os.path.dirname(__file__)

CONFIG_FILE_PATH = os.path.join(ROOT_PATH, 'env.yaml')

if os.path.exists(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, 'r') as file:
        data = yaml.safe_load(file)
else:
    data = dict()

SECRET_KEY = data.get('SECRET_KEY', 'secret_key')

LOG_FILE = data.get('LOG_FILE', 'tmp/output.log')
