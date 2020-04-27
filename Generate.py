from PyQt5 import QtCore, QtGui, QtWidgets


class UserInterface(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setWindowTitle("Generatea")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.only_int = QtGui.QIntValidator()

        MainWindow.setCentralWidget(self.centralWidget)
