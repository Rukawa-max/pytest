import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, \
    QMessageBox, QHBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.label = QLabel('This is a custom widget', self)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('Enter some text...')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton('Open Dialog', self)
        self.button.clicked.connect(self.showDialog)

        self.customWidget = CustomWidget(self)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.customWidget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @pyqtSlot()
    def showDialog(self):
        dialog = CustomDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            text = dialog.lineEdit.text()
            self.customWidget.label.setText(f'You entered: {text}')

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Dialog')
        self.setGeometry(200, 200, 300, 150)

        self.label = QLabel('Enter your name:', self)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('Name...')

        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.accept)

        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.okButton)
        buttonLayout.addWidget(self.cancelButton)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())