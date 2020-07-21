from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class Mail(object):
    def __init__(self, server: str, login: str, password: str, recipient: str, win):
        self._server = server
        self._login = login
        self._password = password
        self._recipient = recipient
        self._win = win

    def send_message(self):
        msg = MIMEMultipart()
        login = self._login
        password = self._password

        msg['From'] = login
        msg['To'] = self._recipient
        msg['Subject'] = self._win.ui.subjectField.text()
        message = self._win.ui.messageField.toPlainText()
        msg.attach(MIMEText(message, 'plain'))

        try:
            sender = smtplib.SMTP(self._server)
            sender.starttls()
            sender.login(login, password)
            sender.sendmail(msg['From'], msg['To'], msg.as_string())
            sender.quit()
        except BaseException as err:
            print(err)
