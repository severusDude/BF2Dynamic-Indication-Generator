import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

from Generate import *
from backup import *
from generateindication import *
from generatedictionary import *


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
        self.all_fstatus = bool()
        self.OPEN_MODE = 'r'
        self.BACKUP_PATH = 'backups'
        self.INDI_PATH = 'HUD\\HudSetup\\Killtext'
        self.DICT_PATH = 'game'
        self.INDEX_START = 1
        self.INDEX_END = 7

        # send input values into declared variables
        self.main_ui.weapon_index_input.textChanged.connect(
            self.weapon_index_act)
        self.main_ui.weapon_name_input.textChanged.connect(
            self.weapon_name_act)
        self.main_ui.weapon_indi_input.textChanged.connect(
            self.weapon_indi_act)

        # connect gen_button to gen_button_act function
        self.main_ui.gen_button.clicked.connect(self.gen_button_act)
        self.main_ui.gen_button.setDisabled(True)

    def gen_button_act(self):
        if self.wep_index and len(self.wep_name) and len(self.wep_indi) > 0:

            self.start_check()

            # action if all required file is checked and exist
            if self.f1_status == True and self.f2_status == True and self.f3_status == True:
                limit = 5
                if BackupFiles(self.INDI_PATH, self.DICT_PATH, limit).compress_succes:
                    self.gen_indi.init(self.wep_index)
                    self.gen_dict.init(
                        self.wep_name, self.wep_index, self.wep_indi)
                    QtWidgets.QMessageBox.information(
                        self, "Succes", "Succes generating scripts\nPlease re-check the files to make sure everything was done correctly")
                else:
                    QtWidgets.QMessageBox.critical(
                        self, "CAUTION", "Automatic backup system is failed to backup.\nFurther generating scripts is cancelled")
                print("not ready")

        else:
            QtWidgets.QMessageBox.warning(
                self, "Error EI_1", "You need to input all the textfield")

    # start checking required files
    def start_check(self):
        # required files location
        att_wep = f'{self.INDI_PATH}\\HudElementsAttackerWeapon.con'
        wep_dict = f"{self.DICT_PATH}\\weapons.py"

        index_list = list()
        index_listed = [temp for temp in range(
            self.INDEX_START, self.INDEX_END)]

        # check HudElementsIndication1-6.con files
        for page in range(self.INDEX_START, self.INDEX_END):
            indi_files = f'HUD\\HudSetup\\Killtext\\HudElementsIndication{page}.con'
            if self.check_file(indi_files):
                index_list.append(page)
            else:
                print(f"error at HudElementsIndication{page}.con")
                QtWidgets.QMessageBox.critical(
                    self, "Error FNE_A_1", f"Error code: A_{page}\n\nRequired file is missing:\n\tHUD\\HudSetup\\Killtext\\HudElementsIndication{page}.con")

        if index_list == index_listed:
            self.f1_status = True
        else:
            self.f1_status = False

        # check HudElementsAttackerWeapon.con
        if self.check_file(att_wep):
            self.f2_status = True
        else:
            self.f2_status = False
            QtWidgets.QMessageBox.critical(
                self, "Error FNE_B_2", f"Error code: B_2\n\nRequired file is missing:\n\tHUD\\HudSetup\\Killtext\\HudElementsAttackerWeapon.con")

        # check weapons.py file
        if self.check_file(wep_dict):
            self.f3_status = True
        else:
            self.f3_status = False
            QtWidgets.QMessageBox.critical(
                self, "Error FNE_C_3", "Error code: C_1\n\nRequired file is missing:\n\tgame\\weapons.py")

        print(self.f1_status)
        print(self.f2_status)
        print(self.f3_status)

    def check_file(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
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
