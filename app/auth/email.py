from flask import render_template, current_app
from config import SMTP
from flask_babel import _
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(subject=_('[MicroBlog] Reset your password'),
               sender=SMTP.email,
               recipient=user.email,
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )
