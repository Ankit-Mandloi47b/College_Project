import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

sender = 'en19cs301055@medicaps.ac.in'
receiver = 'g.dangi0101@gmail.com'
subject = 'licence expiration'
body = 'This is with respect to the expiration of your licence which is to be ended within the month'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))


today = date.today()
today_date = today.strftime('%d%m%Y')


def send_mail(expiry_date):
    if expiry_date - today_date == 30:
        try:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = sender
            smtp_password = 'Ankit@123'
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.starttls()
            smtp_connection.login(smtp_username, smtp_password)
            smtp_connection.sendmail(sender, receiver, message.as_string())
            smtp_connection.quit()
            print('Email sent successfully.')
        except:
            print('error sending mail')
