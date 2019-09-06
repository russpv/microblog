from threading import Thread
from flask_mail import Message
from flask import current_app  # special flask global variable
from app import mail


def send_async_email(app, msg):  # cleaner to pass instance below
    with app.app_context():  # application context needs to be passed to Thread to access email config values
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()  # getcurr() needed to access real app instance within proxy object