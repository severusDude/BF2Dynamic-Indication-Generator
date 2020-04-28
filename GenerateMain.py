from PyQt5 import QtCore, QtGui, QtWidgets
from Generate import *
from generateindication import *
from generatedictionary import *
import qdarkstyle
import sys


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = UserInterface()
        self.main_ui.setupUi(self)
        self.gen_indi = GenerateIndication()
        self.gen_dict = GenerateDictionary()
        self.wep_index = int()
        self.wep_name = str()
        self.wep_indi = str()

        # send input values into declared variables
        self.main_ui.weapon_index_input.textChanged.connect(
            self.weapon_index_act)
        self.main_ui.weapon_name_input.textChanged.connect(
            self.weapon_name_act)
        self.main_ui.weapon_indi_input.textChanged.connect(
            self.weapon_indi_act)

        self.main_ui.gen_button.clicked.connect(self.gen_button_act)

    def gen_button_act(self):
        if self.wep_index and len(self.wep_name) and len(self.wep_indi) > 0:
            self.gen_indi.init(self.wep_index)
            self.gen_dict.init(self.wep_name, self.wep_index, self.wep_indi)
        else:
            self.wep_index = 161
            self.wep_name = "USRIF_M4"
            self.wep_indi = "M4"
            self.gen_indi.init(self.wep_index)
            self.gen_dict.init(self.wep_name, self.wep_index, self.wep_indi)
            # QtWidgets.QMessageBox.warning(
            #     self, "Error", "You need to input all the textfield")

    # def weapon_dict_add(self, file, index, name, indi):
    #     contents = file.readlines()
    #     text_line, req_index = self.find_dict_place(contents, index)
    #     print(text_line)
    #     x = self.line_num_for_phrase_in_file(text_line, file)
    #     print(x)

    #     req_index = int(req_index)
    #     contents.insert(req_index,
    #                     f"		\"{name}\"			 : {index},		 # {indi}")
    #     contents = "".join(contents)
    #     return contents

    # def find_dict_place(self, file, index):
    #     for num, line in enumerate(file, 1):
    #         index_str = index - 1
    #         index_str = str(index_str)
    #         if index_str in line:
    #             print(f"it here {index_str}")
    #             return line, index_str

    # get weapon index from user input
    def weapon_index_act(self, value):
        self.main_ui.gen_button.setDisabled(False)
        if len(value) > 0:
            self.wep_index = value
            self.wep_index = int(self.wep_index)
            print(self.wep_index)
        else:
            None

    # get weapon name from user input
    def weapon_name_act(self, value):
        self.main_ui.gen_button.setDisabled(False)
        if len(value) > 0:
            self.wep_name = value
            print(self.wep_name)
        else:
            None

    # get weapon indication from user input
    def weapon_indi_act(self, value):
        self.main_ui.gen_button.setDisabled(False)
        if len(value) > 0:
            self.wep_indi = value
            print(self.wep_indi)
        else:
            None

    # defining system exception
    def log_uncaught_exceptions(self, ex_cls, ex, tb):
        text = '{}: {}:\n'.format(ex_cls.__name__, ex)
        import traceback
        text += ''.join(traceback.format_tb(tb))

        print(text)
        self.main_ui.QMessageBox.critical(None, 'Error', text)
        quit()

    sys.excepthook = log_uncaught_exceptions


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    program = ControlMainWindow()
    program.show()
    sys.exit(app.exec_())
