
import sys

from PySide import QtCore, QtGui

from src.ui_loader import load_ui_widget


def func():
    print("Hey there jack")


def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = load_ui_widget("src/MainWindow.ui")
    mainWindow.pushButton.connect(QtCore.SIGNAL('clicked()'), func)
    mainWindow.show()

    return app.exec_()

