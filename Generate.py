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

        # generate option labels
        self.gen_option = QtWidgets.QLabel(self.centralWidget)
        self.gen_option.setGeometry(QtCore.QRect(10, 5, 200, 35))
        self.gen_option.setFont(self.label_font)
        self.gen_option.setText("GENERATE OPTION:")
        self.gen_option.setStyleSheet(self.label_style)

        # batch page button
        self.batch_button = QtWidgets.QPushButton(self.centralWidget)
        self.batch_button.setGeometry(QtCore.QRect(140, 45, 125, 35))
        icon = QtGui.QIcon()
        icon.addFile('common\\icons\\batch.ico')
        self.batch_button.setFont(self.button_font)
        self.batch_button.setIcon(icon)
        self.batch_button.setText("BATCH")

        # selected generate option
        self.selected_option = QtWidgets.QLabel(self.centralWidget)
        self.selected_option.setGeometry(QtCore.QRect(190, 5, 200, 35))
        self.selected_option.setFont(self.label_font)
        self.selected_option.setText("SINGLE GENERATE")
        self.selected_option.setStyleSheet(self.label_style)

        # single generation page button
        self.single_button = QtWidgets.QPushButton(self.centralWidget)
        self.single_button.setGeometry(QtCore.QRect(10, 45, 125, 35))
        icon = QtGui.QIcon()
        icon.addFile('common\\icons\\generate.ico')
        self.single_button.setFont(self.button_font)
        self.single_button.setIcon(icon)
        self.single_button.setText("SINGLE")

        ### PAGE 1 ###

        # LABELS
        # weapon index label
        self.weapon_index = QtWidgets.QLabel(self.single_genpage)
        self.weapon_index.setGeometry(QtCore.QRect(10, 80, 155, 35))
        self.weapon_index.setText("WEAPON INDEX")
        self.weapon_index.setFont(self.label_font)

        # weapon name label
        self.weapon_name = QtWidgets.QLabel(self.single_genpage)
        self.weapon_name.setGeometry(QtCore.QRect(10, 155, 155, 35))
        self.weapon_name.setText("WEAPON NAME")
        self.weapon_name.setFont(self.label_font)

        # weapon indication label
        self.weapon_indi = QtWidgets.QLabel(self.single_genpage)
        self.weapon_indi.setGeometry(QtCore.QRect(10, 230, 200, 35))
        self.weapon_indi.setText("WEAPON INDICATION")
        self.weapon_indi.setFont(self.label_font)

        self.texture_label1 = QtWidgets.QLabel(self.single_genpage)
        self.texture_label1.setGeometry(QtCore.QRect(165, 315, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.texture_label1.setFont(font)
        self.texture_label1.setText("Generate Texture")

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
        # self.weapon_indi_input.setMaxLength(7)

        # BUTTONS
        # generate button
        self.gen_button = QtWidgets.QPushButton(self.single_genpage)
        self.gen_button.setGeometry(QtCore.QRect(10, 315, 125, 35))
        icon = QtGui.QIcon()
        icon.addFile('common\\icons\\generate.ico')
        self.gen_button.setIcon(icon)
        self.gen_button.setText("GENERATE")
        self.gen_button.setFont(self.button_font)

        self.gen_texture1 = QtWidgets.QCheckBox(self.single_genpage)
        self.gen_texture1.setGeometry(QtCore.QRect(140, 318, 20, 20))

        ### PAGE 2 ###

        # LABELS
        # file status label
        self.batch_filepath = QtWidgets.QLabel(self.batch_genpage)
        self.batch_filepath.setGeometry(QtCore.QRect(10, 160, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(55)
        stylesheet = """
        QWidget {
            background: gray solid;
            border: 1px solid black;
            border-radius: 4px;
        }
        """
        self.batch_filepath.setMaximumWidth(480)
        self.batch_filepath.setFont(font)
        self.batch_filepath.setStyleSheet(stylesheet)

        # show requirment for selected batch file
        self.batch_active = QtWidgets.QLabel(self.batch_genpage)
        self.batch_active.setGeometry(QtCore.QRect(140, 115, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.batch_active.setFont(font)
        self.batch_active.setText("No file is selected")

        # index_start input label
        self.index_label = QtWidgets.QLabel(self.batch_genpage)
        self.index_label.setGeometry(QtCore.QRect(10, 185, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.index_label.setFont(font)
        self.index_label.setText("Start index")
        self.index_label.setDisabled(True)
        
        # generate script label
        self.script_label2 = QtWidgets.QLabel(self.batch_genpage)
        self.script_label2.setGeometry(QtCore.QRect(135, 185, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.script_label2.setFont(font)
        self.script_label2.setText("Generate Script")
        self.script_label2.setDisabled(True)

        # generate texture label
        self.texture_label2 = QtWidgets.QLabel(self.batch_genpage)
        self.texture_label2.setGeometry(QtCore.QRect(135, 215, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.texture_label2.setFont(font)
        self.texture_label2.setText("Generate Texture")
        self.texture_label2.setDisabled(True)

        # label console
        self.console_label = QtWidgets.QLabel(self.batch_genpage)
        self.console_label.setGeometry(QtCore.QRect(10, 290, 155, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(60)
        self.console_label.setFont(font)
        self.console_label.setText("Console Log")

        # BUTTONS
        # choose file button
        self.choose_batchfile = QtWidgets.QPushButton(self.batch_genpage)
        self.choose_batchfile.setGeometry(QtCore.QRect(10, 120, 125, 35))
        self.choose_batchfile.setFont(self.button_font)
        icon = QtGui.QIcon()
        icon.addFile('common\\icons\\addfile.png')
        self.choose_batchfile.setText("OPEN FILE")
        self.choose_batchfile.setIcon(icon)

        # start batch button
        self.start_batch = QtWidgets.QPushButton(self.batch_genpage)
        self.start_batch.setGeometry(QtCore.QRect(10, 255, 125, 35))
        self.start_batch.setFont(self.button_font)
        self.start_batch.setText("START BATCH")
        self.start_batch.setDisabled(True)

        # link to guide button
        self.batch_guide = QtWidgets.QPushButton(self.batch_genpage)
        self.batch_guide.setGeometry(QtCore.QRect(270, 42, 85, 35))
        icon = QtGui.QIcon()
        icon.addFile("common\\icons\\info.png")
        self.batch_guide.setFont(self.button_font)
        self.batch_guide.setIcon(icon)
        self.batch_guide.setToolTip(
            "Guide to make your own batch set or generate an existing one")
        self.batch_guide.setText("GUIDE")

        # check if user want to generate script
        self.gen_script2 = QtWidgets.QCheckBox(self.batch_genpage)
        self.gen_script2.setGeometry(QtCore.QRect(110, 188, 20, 20))
        self.gen_script2.setChecked(True)
        self.gen_script2.setDisabled(True)

        # check if user want to generate texture
        self.gen_texture2 = QtWidgets.QCheckBox(self.batch_genpage)
        self.gen_texture2.setGeometry(QtCore.QRect(110, 218, 20, 20))
        self.gen_texture2.setDisabled(True)

        # INPUTs
        # index_start
        self.index_start = QtWidgets.QLineEdit(self.batch_genpage)
        self.index_start.setGeometry(QtCore.QRect(10, 215, 45, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(55)
        self.index_start.setToolTip(
            "Starting index of your batch set, ex: 161")
        self.index_start.setFont(font)
        self.index_start.setValidator(self.only_int)
        self.index_start.setDisabled(True)

        # Console
        # console window
        self.console_window = QtWidgets.QListWidget(self.batch_genpage)
        self.console_window.setGeometry(QtCore.QRect(10, 315, 480, 125))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(55)
        self.console_window.setFont(font)

        MainWindow.setCentralWidget(self.centralWidget)

        self.gen_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
