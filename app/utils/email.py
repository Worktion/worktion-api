"""
Author: Victor Manuel Niño Martínez
Creation: 12/03/2021
Last update: 13/03/2021
"""
from smtplib import SMTPException
from django.core.mail import send_mail
from django.template import loader
from app.settings import EMAIL_HOST_USER

CONFIRMATION_EMAIL_MESSAGE = "Confirmación de correo electrónico"


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
        subject = CONFIRMATION_EMAIL_MESSAGE
        message = ""
        message_html = loader.render_to_string(
            'ConfirmationEmail.html',
            {
                'user_name': user.first_name + " " + user.last_name,
                'token': token
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
