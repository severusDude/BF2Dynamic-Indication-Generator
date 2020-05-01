from PyQt5 import QtCore, QtGui, QtWidgets


class UserInterface(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setWindowTitle("Crypter")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.only_int = QtGui.QIntValidator()

        self.gen_page = QtWidgets.QStackedWidget(self.centralWidget)
        self.gen_page.setGeometry(QtCore.QRect(0, 0, 500, 450))

        self.single_genpage = QtWidgets.QWidget()
        self.batch_genpage = QtWidgets.QWidget()
        self.gen_page.addWidget(self.single_genpage)
        self.gen_page.addWidget(self.batch_genpage)

        # STYLE
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

        self.label_style = """
        QWidget {
            color: green;
        }
        """

        # LABELS
        # generate option labels
        self.gen_option = QtWidgets.QLabel(self.centralWidget)
        self.gen_option.setGeometry(QtCore.QRect(10, 5, 200, 35))
        self.gen_option.setFont(self.label_font)
        self.gen_option.setText("GENERATE OPTION:")
        self.gen_option.setStyleSheet(self.label_style)

        # selected generate option
        self.selected_option = QtWidgets.QLabel(self.centralWidget)
        self.selected_option.setGeometry(QtCore.QRect(190, 5, 200, 35))
        self.selected_option.setFont(self.label_font)
        self.selected_option.setText("SINGLE GENERATION")
        self.selected_option.setStyleSheet(self.label_style)

        # weapon index label
        self.weapon_index = QtWidgets.QLabel(self.single_genpage)
        self.weapon_index.setGeometry(QtCore.QRect(10, 80, 155, 35))
        self.weapon_index.setText("WEAPON INDEX")
        self.weapon_index.setFont(self.label_font)
        self.weapon_index.setStyleSheet(self.label_style)

        # weapon name label
        self.weapon_name = QtWidgets.QLabel(self.single_genpage)
        self.weapon_name.setGeometry(QtCore.QRect(10, 155, 155, 35))
        self.weapon_name.setText("WEAPON NAME")
        self.weapon_name.setFont(self.label_font)
        self.weapon_name.setStyleSheet(self.label_style)

        # weapon indication label
        self.weapon_indi = QtWidgets.QLabel(self.single_genpage)
        self.weapon_indi.setGeometry(QtCore.QRect(10, 230, 200, 35))
        self.weapon_indi.setText("WEAPON INDICATION")
        self.weapon_indi.setFont(self.label_font)
        self.weapon_indi.setStyleSheet(self.label_style)

        # INPUTS
        # weapon index input
        self.weapon_index_input = QtWidgets.QLineEdit(self.single_genpage)
        self.weapon_index_input.setGeometry(QtCore.QRect(10, 120, 365, 35))
        self.weapon_index_input.setPlaceholderText("Example: 161")
        self.weapon_index_input.setFont(self.input_font)
        self.weapon_index_input.setValidator(self.only_int)

        # weapon name input
        self.weapon_name_input = QtWidgets.QLineEdit(self.single_genpage)
        self.weapon_name_input.setGeometry(QtCore.QRect(10, 195, 365, 35))
        self.weapon_name_input.setPlaceholderText("Example: USRIF_M4")
        self.weapon_name_input.setFont(self.input_font)

        # weapon indication input
        self.weapon_indi_input = QtWidgets.QLineEdit(self.single_genpage)
        self.weapon_indi_input.setGeometry(QtCore.QRect(10, 270, 365, 35))
        self.weapon_indi_input.setPlaceholderText("Example: M4")
        self.weapon_indi_input.setFont(self.input_font)
        self.weapon_indi_input.setMaxLength(7)

        # BUTTONS
        self.gen_button = QtWidgets.QPushButton(self.single_genpage)
        self.gen_button.setGeometry(QtCore.QRect(10, 315, 125, 35))
        icon = QtGui.QIcon()
        icon.addFile('common\\icons\\generate.ico')
        self.gen_button.setIcon(icon)
        self.gen_button.setText("GENERATE")
        self.gen_button.setFont(self.button_font)

        self.single_button = QtWidgets.QPushButton(self.centralWidget)
        self.single_button.setGeometry(QtCore.QRect(10, 45, 125, 35))
        self.single_button.setText("SINGLE")
        self.single_button.setFont(self.button_font)

        self.batch_button = QtWidgets.QPushButton(self.centralWidget)
        self.batch_button.setGeometry(QtCore.QRect(140, 45, 125, 35))
        self.batch_button.setText("BATCH")
        self.batch_button.setFont(self.button_font)

        MainWindow.setCentralWidget(self.centralWidget)

        self.gen_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
