# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8a9cc19a83e70624743e6a70b4666055'
auth_token = '6eb914d59682e890f1f0336054173dbf'
def sendMessage(mensaje):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=mensaje,
                                from_='+12695750010',
                                media_url='https://demo.twilio.com/owl.png',
                                to='+56968583627'
                            )