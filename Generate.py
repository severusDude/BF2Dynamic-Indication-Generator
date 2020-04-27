from PyQt5 import QtCore, QtGui, QtWidgets


class UserInterface(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setWindowTitle("Generatea")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.only_int = QtGui.QIntValidator()

        # FONTS
        self.label_font = QtGui.QFont()
        self.label_font.setFamily("Quicksand")
        self.label_font.setPointSize(14)
        self.label_font.setBold(True)
        self.label_font.setWeight(75)

        self.input_font = QtGui.QFont()
        self.input_font.setFamily("Quicksand")
        self.input_font.setPointSize(13)
        self.input_font.setBold(True)
        self.input_font.setWeight(75)

        self.button_font = QtGui.QFont()
        self.button_font.setFamily("Quicksand")
        self.button_font.setPointSize(13)
        self.button_font.setBold(True)
        self.button_font.setWeight(75)

        # LABELS
        # weapon index label
        self.weapon_index = QtWidgets.QLabel(self.centralWidget)
        self.weapon_index.setGeometry(QtCore.QRect(10, 20, 155, 35))
        self.weapon_index.setText("WEAPON INDEX")
        self.weapon_index.setFont(self.label_font)
        self.weapon_index.setStyleSheet("""
        QWidget {
            color: green;
        }
        """)

        # weapon name label
        self.weapon_name = QtWidgets.QLabel(self.centralWidget)
        self.weapon_name.setGeometry(QtCore.QRect(10, 95, 155, 35))
        self.weapon_name.setText("WEAPON NAME")
        self.weapon_name.setFont(self.label_font)
        self.weapon_name.setStyleSheet("""
        QWidget {
            color: green;
        }
        """)

        # weapon indication label
        self.weapon_indi = QtWidgets.QLabel(self.centralWidget)
        self.weapon_indi.setGeometry(QtCore.QRect(10, 170, 200, 35))
        self.weapon_indi.setText("WEAPON INDICATION")
        self.weapon_indi.setFont(self.label_font)
        self.weapon_indi.setStyleSheet("""
        QWidget {
            color: green;
        }
        """)

        MainWindow.setCentralWidget(self.centralWidget)
