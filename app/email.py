import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template
from app import mail, app
from config import SMTP
from threading import Thread
from app import log


def send_async_email(app, msg, recipients):
    with app.app_context():
        try:
            smtp = smtplib.SMTP(host=SMTP.host,
                                port=SMTP.port,
                                timeout=5)
            smtp.starttls()
            smtp.login(SMTP.email, SMTP.password)
            response = smtp.sendmail(
                from_addr=SMTP.email,
                to_addrs=recipients,
                msg=msg.as_string()
            )
        except Exception as e:
            log.info('Cant send reset password mail, user: %s, cause: %s'
                     % (recipients, str(e)))


def send_email(subject, sender, recipient, text_body, html_body):
    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText(text_body, 'plain'))
    msg.attach(MIMEText(html_body, 'html'))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    Thread(target=send_async_email, args=(app, msg, recipient)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(subject='Reset your password',
               sender=SMTP.email,
               recipient=user.email,
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )
