# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='novasweetie0507@gmail.com',
    to_emails='dsweetykumari7@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg =SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)