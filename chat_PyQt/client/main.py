import sys


from functools import partial
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTextBrowser,
                             QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout, QPushButton, QTextEdit, QCompleter)
from PyQt5.QtCore import QThread
from socket import *
from threading import Thread


class ReceptionThread(Thread):
    def __init__(self, window, sock, parent=None):
        super().__init__()
        self.window = window
        self.sock = sock

    def run(self):
        while True:
            server_resp = self.sock.recv(1000)
            self.rec_msg = server_resp.decode()
            self.update_list_message(self.rec_msg)

            if 'disconnected' in self.rec_msg:
                self.sock.close()

    def update_list_message(self, text_msg):

        self.window.box_check_text.append(text_msg)


class ClientView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.sock = None

        self.setWindowTitle('client')
        self.setFixedSize(500, 500)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.main_layout = QVBoxLayout()
        self._central_widget.setLayout(self.main_layout)

        self._create_display_ip()
        self.__create_display_name()
        self._create_display()
        self._create_list_message()

    def _create_display_ip(self):
        self.add_ip_widget = QHBoxLayout()

        self.display_ip = QLineEdit()
        self.display_ip.setFixedSize(150, 35)
        self.display_ip.setStyleSheet('font-size: 15pt; color: black')
        self.display_ip.setPlaceholderText('ip')

        self.display_port = QLineEdit()
        self.display_port.setFixedSize(150, 35)
        self.display_port.setStyleSheet('font-size: 15pt; color: black')
        self.display_port.setPlaceholderText('port')

        self.connection_button = QPushButton("connect")
        self.connection_button.setFixedSize(100, 35)
        self.connection_button.setStyleSheet('font-size: 15pt; color: black')
        self.connection_button.clicked.connect(partial(self.connection_ip))

        self.add_ip_widget.addWidget(self.display_ip)
        self.add_ip_widget.addWidget(self.display_port)
        self.add_ip_widget.addWidget(self.connection_button)
        self.add_ip_widget.addStretch(0)

        self.main_layout.addLayout(self.add_ip_widget)

    def __create_display_name(self):
        self.add_name_widget = QHBoxLayout()

        self.display_name = QLineEdit()
        self.display_name.setFixedSize(200, 35)
        self.display_name.setStyleSheet('font-size: 15pt; color: black')
        self.display_name.setPlaceholderText('name')

        self.up_button = QPushButton("up")
        self.up_button.setFixedSize(45, 35)
        self.up_button.setStyleSheet('font-size: 15pt; color: black')
        self.up_button.clicked.connect(partial(self.send_new_name))

        self.add_name_widget.addWidget(self.display_name)
        self.add_name_widget.addWidget(self.up_button)
        self.add_name_widget.addStretch(0)

        self.main_layout.addLayout(self.add_name_widget)

    def _create_display(self):
        self.add_text_widget = QHBoxLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setStyleSheet('font-size: 20pt; color: black')
        self.display.setPlaceholderText("your message")

        self.send_button = QPushButton("Send")
        self.send_button.setFixedSize(70, 40)
        self.send_button.setStyleSheet('font-size: 20pt; color: black')
        self.send_button.clicked.connect(partial(self.send_message))

        self.add_text_widget.addWidget(self.display)
        self.add_text_widget.addWidget(self.send_button)

        self.main_layout.addLayout(self.add_text_widget)

    def _create_list_message(self):

        self.box_check_text = QTextBrowser()
        self.box_check_text.setStyleSheet('font-size: 15pt; color: blue')

        self.main_layout.addWidget(self.box_check_text)


    def connection_ip(self):
        ip = self.display_ip.text()
        port = self.display_port.text()
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((f'{ip}', int(port)))
            self.box_check_text.append(f"connection server {ip}: {port}")

            self.ResMsg = ReceptionThread(window=self, sock=self.sock)
            self.ResMsg.start()
        except:
            self.display_ip.setText('ip')
            self.display_port.setText('port')

    def send_new_name(self):
        if self.sock:
            message = f'command:change_name:{self.display_name.text()}'
            self.sock.send(message.encode())
        else:
            self.box_check_text.append(f"Not connection")

    def send_message(self):
        if self.sock:
            message = self.display.text()
            self.sock.send(message.encode())
            self.display.setText('')
        else:
            self.box_check_text.append(f"Not connection")


def main():

    app = QApplication(sys.argv)

    view = ClientView()

    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
