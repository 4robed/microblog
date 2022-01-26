import logging
import os
from config import ROOT_PATH, LOG_FILE, SMTP
from logging.handlers import RotatingFileHandler, SMTPHandler


class SetLog():
    log = logging.getLogger('error')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s [in %(pathname)s:%(lineno)d]')
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    log.setLevel(logging.INFO)
    log.addHandler(logHandler)

    def file_log(self):
        if not os.path.exists(os.path.join('tmp')):
            os.mkdir('tmp')
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        self.log.addHandler(file_handler)
        self.log.info('Microblog startup')

    def mail_log(self):
        if SMTP.host:
            auth = None
            if SMTP.email or SMTP.password:
                auth = (SMTP.email, SMTP.password)
            secure = ()
            mail_handler = SMTPHandler(
                mailhost=(SMTP.email, SMTP.password),
                fromaddr='no-reply' + SMTP.host,
                toaddrs=SMTP.app_name, subject='Microblog Failure',
                credentials=auth, secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            self.log.addHandler(mail_handler)
