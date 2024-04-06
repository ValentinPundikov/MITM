import time
from PyQt6 import QtCore, QtWidgets


class Ui_DiffHell(object):
    def setupUi(self, DiffHell):
        DiffHell.setObjectName("DiffHell")
        DiffHell.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(DiffHell)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_p = QtWidgets.QLabel(self.centralwidget)
        self.label_p.setText("Число P:")
        self.gridLayout.addWidget(self.label_p, 0, 0, 1, 1)
        self.lineEdit_p = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_p, 0, 1, 1, 1)

        self.label_g = QtWidgets.QLabel(self.centralwidget)
        self.label_g.setText("Число G:")
        self.gridLayout.addWidget(self.label_g, 1, 0, 1, 1)
        self.lineEdit_g = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_g, 1, 1, 1, 1)

        self.label_secret1 = QtWidgets.QLabel(self.centralwidget)
        self.label_secret1.setText("Секретный ключ 1:")
        self.gridLayout.addWidget(self.label_secret1, 2, 0, 1, 1)
        self.lineEdit_secret1 = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_secret1, 2, 1, 1, 1)

        self.label_secret2 = QtWidgets.QLabel(self.centralwidget)
        self.label_secret2.setText("Секретный ключ 2:")
        self.gridLayout.addWidget(self.label_secret2, 3, 0, 1, 1)
        self.lineEdit_secret2 = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_secret2, 3, 1, 1, 1)

        self.label_interval = QtWidgets.QLabel(self.centralwidget)
        self.label_interval.setText("Максимальный интервал (мкс):")
        self.gridLayout.addWidget(self.label_interval, 4, 0, 1, 1)
        self.lineEdit_interval = QtWidgets.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit_interval, 4, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("Запустить")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.textEdit, 6, 0, 1, 2)

        DiffHell.setCentralWidget(self.centralwidget)

        self.retranslateUi(DiffHell)
        QtCore.QMetaObject.connectSlotsByName(DiffHell)

        self.pushButton.clicked.connect(self.start_dh_exchange)

    def retranslateUi(self, DiffHell):
        _translate = QtCore.QCoreApplication.translate
        DiffHell.setWindowTitle(_translate("DiffHell", "DiffHell"))

    def start_dh_exchange(self):
        p = int(self.lineEdit_p.text())
        g = int(self.lineEdit_g.text())
        secret1 = int(self.lineEdit_secret1.text())
        secret2 = int(self.lineEdit_secret2.text())
        max_interval = int(self.lineEdit_interval.text())

        def calculate_shared_key(p, g, secret):
            return pow(g, secret, p)

        shared_key1 = calculate_shared_key(p, g, secret1)

        shared_key2 = calculate_shared_key(p, g, secret2)

        def exchange_bits():
            time.sleep(0.000001)

        start_time = time.time()
        exchange_bits()
        end_time = time.time()
        exchange_time1 = (end_time - start_time) * 1000000  # в микросекундах

        start_time = time.time()
        exchange_bits()
        end_time = time.time()
        exchange_time2 = (end_time - start_time) * 1000000  # в микросекундах

        if exchange_time1 > max_interval or exchange_time2 > max_interval:
            self.textEdit.setText("Превышен максимальный интервал для обмена данными")
        else:
            self.textEdit.setText(f"Общий секретный ключ: {shared_key1}")
            self.textEdit.append(f"Время обмена битами со стороны 1: {exchange_time1} мкс")
            self.textEdit.append(f"Время обмена битами со стороны 2: {exchange_time2} мкс")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiffHell = QtWidgets.QMainWindow()
    ui = Ui_DiffHell()
    ui.setupUi(DiffHell)
    DiffHell.show()
    sys.exit(app.exec())