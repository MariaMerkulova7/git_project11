import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
import requests

class My_Project(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Большая задача по Maps API")
        self.setStyleSheet("background-color: rgb(177, 179, 222)")
        self.setGeometry(500, 500, 500, 500)
        self.setMaximumSize(500, 500)
        self.setMinimumSize(500, 500)

        self.my_map = QLabel(self)
        tmp = self.my_map.resize(300, 300)
        tmp = self.my_map.move(100, 100)

        self.x = 37.620070
        self.y = 55.753630
        self.sizexy = 300

        request = f"https://static-maps.yandex.ru/1.x/?ll={self.x},{self.y}&size={self.sizexy},{self.sizexy}"





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My_Project()
    ex.show()
    sys.exit(app.exec())
