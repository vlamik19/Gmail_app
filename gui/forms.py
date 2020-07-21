from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from lib.classes import Mail


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('mainWindow.ui')
        self._mail = None
        self._password = self._ui.passwordFile
        self._password.setEchoMode(self._ui.passwordFile.Password)
        self._ui.sendButton.clicked.connect(self.send_message)
        self._ui.clearButton.clicked.connect(self.clear_message)
        self._ui.groupButton.clicked.connect(self.add_group)
        self._ui.adressButton.clicked.connect(self.add_mail)

    @property
    def ui(self):
        return self._ui

    def open(self):
        self._ui.show()

    def get_params(self):
        """ Метод для получения параметров """
        server = self._ui.serverField.text()
        login = self._ui.SenderField.text()
        password = self._ui.passwordFile.text()
        recipient = self._ui.recipientField.text()
        if server == '':
            QMessageBox.warning(self, 'Warning', 'Поле "MSTP-Server" не должно быть пустым!')
        elif login == '':
            QMessageBox.warning(self, 'Warning', 'Поле "Отправитель" не должно быть пустым!')
        elif password == '':
            QMessageBox.warning(self, 'Warning', 'Поле "Файл пароля" не должно быть пустым')
        elif recipient == '':
            QMessageBox.warning(self, 'Warning', 'Поле "Получатель" не должно быть пустым')
        else:
            try:
                return server, login, password, recipient
            except BaseException as err:
                QMessageBox.warning(self, 'Warning', str(err))
        return '', '', '', ''

    def send_message(self):
        """ Метод отправки сообщения на электроную почту """
        server, login, password, recipient = self.get_params()
        if server != '' and login != '' and password != '' and recipient != '':
            self._mail = Mail(server, login, password, recipient, self)
            self._mail.send_message()
            QMessageBox.information(self, 'Information', 'Сообщение успешно отправлено!')

    def clear_message(self):
        """ Метод который стирает данные с рабочей панели"""
        question = QMessageBox.question(self, 'Question', 'Вы действительно хотите стереть все данные')
        if question == QMessageBox.Yes:
            QMessageBox.information(self, 'Information', 'Все данные успешно стёрты')
            self._ui.serverField.setText('')
            self._ui.SenderField.setText('')
            self._ui.passwordFile.setText('')
            self._ui.recipientField.setText('')
            self._ui.copiesList.setText('')
            self._ui.subjectField.setText('')
            self._ui.messageField.setText('')

    def add_group(self):
        QMessageBox.information(self, 'Test', 'add_group ok!')

    def add_mail(self):
        QMessageBox.information(self, 'Test', 'add_mail ok!')
