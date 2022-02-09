from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.common.utils import SetLog
from flask_mail import Mail
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

if not app.debug:
    log = SetLog()
    log.file_log()
    log.mail_log()

log = SetLog().log

from app import routes, models, errors
