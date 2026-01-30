"""."""
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Я наконец научился отправлять письма с помощью Python!!!!'
msg["From"] = ''
msg["To"] = ''
msg.preamble = 'wtf is this'
cont = """Я это сделал и прикрепил в питоне!!!!
УРАААААА!!!
☺☺☺ :)"""
msg.set_content(cont)
with open('Автобаза. Сертификат. Иванов Иван Иванович.pdf', 'rb') as cert:
    cert_info = cert.read()
msg.add_attachment(cert_info, maintype='document',
                   subtype='pdf',
                   filename='Автобаза. Сертификат. Иванов Иван Иванович.pdf')


# smtp.[адрес почты], второй 587 по стандарту шифрования TSL
# Либо, очень редко, 465
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
# шифровка
smtpobj.starttls()
# login (emailer_app password)
smtpobj.login('', '')
message = """
Subject: hiii
lololo
qwerty
"""
# smtpobj.sendmail('testy.thingy31@gmail.com', 'enlearn46@gmail.com', message)
smtpobj.send_message(msg)
