from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.common.utils import SetLog
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from app.errors import bp as errors_bp
from app.auth import bp as auth_bp
import config


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth_login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(errors_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    if not app.debug and not app.testing:
        log = SetLog()
        log.file_log()
        log.mail_log()
    return app


@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'vi'


from app import models
from app.auth import routes
