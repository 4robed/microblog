from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail


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
            print('Cant send reset password mail, user: %s, cause: %s'
                     % (recipients, str(e)))


def send_email(subject, sender, recipient, text_body, html_body):
    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText(text_body, 'plain'))
    msg.attach(MIMEText(html_body, 'html'))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg, recipient)).start()
