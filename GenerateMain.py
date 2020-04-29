from PyQt5 import QtCore, QtGui, QtWidgets
from Generate import *
from generateindication import *
from generatedictionary import *
import qdarkstyle
import sys
import os


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
        self.f1_status = bool()
        self.f2_status = bool()
        self.f3_status = bool()

        # send input values into declared variables
        self.main_ui.weapon_index_input.textChanged.connect(
            self.weapon_index_act)
        self.main_ui.weapon_name_input.textChanged.connect(
            self.weapon_name_act)
        self.main_ui.weapon_indi_input.textChanged.connect(
            self.weapon_indi_act)

        # connect gen_button to gen_button_act function
        self.main_ui.gen_button.clicked.connect(self.gen_button_act)

    def gen_button_act(self):
        if self.wep_index and len(self.wep_name) and len(self.wep_indi) > 0:
            # over complicated lol
            att_wep = "HUD\\HudSetup\\Killtext\\HudElementsAttackerWeapon.con"
            wep_dict = "game\\weapons.py"
            read_file = 'r+'
            for page in range(1, 7):
                if self.find_file(f'HUD\\HudSetup\\Killtext\\HudElementsIndication{page}.con', read_file):
                    self.f1_status = True
                else:
                    self.f1_status = False
                    QtWidgets.QMessageBox.warning(
                        self, "Error 1", f"Error code: 1\nIndication{page} files not found")

            if self.find_file(att_wep, read_file):
                self.f2_status = True
            else:
                self.f2_status = False
                QtWidgets.QMessageBox.warning(
                    self, "Error 2", f"Error code: 2\nAttackerWeapon file not found")

            if self.find_file(wep_dict, read_file):
                self.f3_status = True
            else:
                self.f3_status = False
                QtWidgets.QMessageBox.warning(
                    self, "Error 3", "Error code: 3\nweapons.py file not found")

            if self.f1_status == True and self.f2_status == True and self.f3_status == True:
                self.gen_indi.init(self.wep_index)
                self.gen_dict.init(
                    self.wep_name, self.wep_index, self.wep_indi)

        else:
            QtWidgets.QMessageBox.warning(
                self, "Error", "You need to input all the textfield")

    def find_file(self, file, open_mode):
        try:
            with open(file, open_mode) as file_read:
                return True
        except FileNotFoundError as e:
            print(
                f"Exception FileNotFoundError\nOpened file: {file}\nOriginal: {e}")
            return False

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
