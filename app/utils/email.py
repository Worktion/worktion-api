"""
Author: Victor Manuel Niño Martínez
Creation: 12/03/2021
Last update: 20/03/2021
"""
from smtplib import SMTPException
import os
from django.core.mail import send_mail
from django.template import loader
from app.settings import EMAIL_HOST_USER

CONFIRMATION_EMAIL_SUBJECT = "Confirmación de correo electrónico"
RECOVER_PASSWORD_SUBJECT = "Restablece tu contraseña de Worktion"


class Email:
    """ Custom class to send emails """

    def __init__(self, subject, message, client, custom_message_html):
        self.subject = subject
        self.message = message
        self.email_host = EMAIL_HOST_USER
        self.client = [client]
        self.custom_html_message = custom_message_html

    @classmethod
    def send_confirmation_register(cls, user, token):
        """ Public method to send a confirmation email """
        subject = CONFIRMATION_EMAIL_SUBJECT
        message = ""
        message_html = loader.render_to_string(
            'ConfirmationEmail.html',
            {
                'user_name': user.first_name + " " + user.last_name,
                'base_url': os.environ.get("BASE_URL_WEB_CLIENT", "http://localhost:3000"),
                'token': token
            }
        )
        email = Email(subject, message, user.email, message_html)
        try:
            email.send_mail()
        except Exception as ex:
            raise ex

    @classmethod
    def send_recover_password(cls, user):
        """ Public method to send a email to recover password """
        subject = RECOVER_PASSWORD_SUBJECT
        message = ""
        message_html = loader.render_to_string(
            'RecoverPassword.html',
            {
                'user_name': user.first_name + " " + user.last_name,
                'code': user.code_recover_password,
            }
        )
        email = Email(subject, message, user.email, message_html)
        try:
            email.send_mail()
        except Exception as ex:
            raise ex

    def send_mail(self):
        """ Method that send the email """
        try:
            send_mail(
                subject=self.subject,
                message=self.message,
                from_email=self.email_host,
                recipient_list=self.client,
                fail_silently=False,
                html_message=self.custom_html_message,
            )
        except SMTPException as ex:
            raise Exception from ex
