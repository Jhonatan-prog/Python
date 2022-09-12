from email.message import EmailMessage
import ssl
import smtplib

sender = input('write your email over here please: ')
Email_sender = sender

## password = bnoxcsowipxqnfov
password = input('write your email-password over here please: ')
Email_password = password

receiver = input('Who are you sending the info to?: ')
Email_receiver = receiver

subject = "Practice more and more"
content = """"
    The more you practice the easier you will solve
    the problems.
"""

email = EmailMessage()
email['FROM'] = Email_sender
email['TO'] = Email_receiver
email['subject'] = subject
email.set_content(content)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(Email_sender, Email_password)
    smtp.sendmail(Email_sender, Email_receiver, email.as_string())