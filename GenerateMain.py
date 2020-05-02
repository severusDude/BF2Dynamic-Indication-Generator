import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

from Generate import *
from backup import *
from batch import *
from generateindication import *
from generatedictionary import *


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = UserInterface()
        self.main_ui.setupUi(self)
        self.gen_indi = GenerateIndication()
        self.gen_dict = GenerateDictionary()
        self.batchset_index = int()
        self.wep_index = int()
        self.wep_name = str()
        self.wep_indi = str()
        self.f1_status = bool()
        self.f2_status = bool()
        self.f3_status = bool()
        self.batch_contents = str()
        self.is_active = bool()
        self.OPTION_1 = "SINGLE GENERATE"
        self.OPTION_2 = "BATCH PROCESSING"
        self.OPEN_MODE = 'r'
        self.BACKUP_PATH = 'backups'
        self.INDI_PATH = 'HUD\\HudSetup\\Killtext'
        self.DICT_PATH = 'game'
        self.ACTIVATION_KEY = "activate"
        self.INDEX_START = 1
        self.INDEX_END = 7
        self.BACKUP_FILELIMIT = 5

        # send input values into declared variables
        self.main_ui.weapon_index_input.textChanged.connect(
            self.weapon_index_act)
        self.main_ui.weapon_name_input.textChanged.connect(
            self.weapon_name_act)
        self.main_ui.weapon_indi_input.textChanged.connect(
            self.weapon_indi_act)
        self.main_ui.index_start.textChanged.connect(self.get_index_start)

        # connect gen_button to gen_button_act function
        self.main_ui.gen_button.clicked.connect(self.gen_button_act)

        # open a batch set
        self.main_ui.choose_batchfile.clicked.connect(self.open_file)

        # start batch from opened batch set
        self.main_ui.start_batch.clicked.connect(self.start_batch)

        # page switcher
        self.main_ui.single_button.clicked.connect(
            lambda: self.page_switcher(0))
        self.main_ui.batch_button.clicked.connect(
            lambda: self.page_switcher(1))

    # switch page and show page name
    def page_switcher(self, to_page):
        self.main_ui.gen_page.setCurrentIndex(to_page)

        page = self.main_ui.gen_page.currentIndex()
        if page == 0:
            self.main_ui.selected_option.setText(self.OPTION_1)
        else:
            self.main_ui.selected_option.setText(self.OPTION_2)

    # open batch file
    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open batch file", "", "*.txt", options=options)
        if filename:
            self.main_ui.batch_filepath.setText(filename)
            self.main_ui.batch_filepath.adjustSize()
            self.main_ui.console_window.addItem(f"Open batch set: {filename}")

            with open(filename, self.OPEN_MODE) as f:
                self.batch_contents = f.readlines()

            self.batch_isactive(filename)

    def batch_isactive(self, batch_filepath):
        key = self.batch_contents[0]
        key = key.replace('\n', '')
        print(key)

        if key == self.ACTIVATION_KEY:
            self.is_active = True
            self.batch_active()

        else:
            self.is_active = False
            self.batch_active()

    def batch_active(self):

        if self.is_active:

            self.main_ui.batch_active.setText("Batch file is active")
            self.main_ui.batch_active.adjustSize()

            self.main_ui.index_start.setDisabled(False)
            self.main_ui.index_label.setDisabled(False)

            self.batchset_items = BatchProcessing(
                self.batch_contents, self.is_active)

            self.main_ui.console_window.addItem(
                f"Found {len(self.batchset_items.items)} valid items from batch set:")

            for item in self.batchset_items.items:
                self.main_ui.console_window.addItem(f"    {item}")

        else:

            self.main_ui.batch_active.setText(
                "Batch file is not active,\nplease see guide to make your own batch set")
            self.main_ui.batch_active.adjustSize()

    def start_batch(self):

        # get name items
        self.batch_itemcount = len(self.batchset_items.items)
        last_index = self.batchset_index + self.batch_itemcount
        name_list = self.batchset_items.name_items
        key_list = self.batchset_items.key_items

        count_index = self.batchset_index

        if BackupFiles(self.INDI_PATH, self.DICT_PATH, self.BACKUP_FILELIMIT).compress_succes:

            # generate indication from batch set
            for item in range(self.batchset_index, last_index):
                self.gen_indi.init(item)
                self.main_ui.console_window.addItem(
                    f"Added index {item} into Indication Files")

            for item_name, item_key, item_index in zip(name_list, key_list, range(self.batchset_index, last_index)):
                self.gen_dict.init(item_key, item_index, item_name)
                self.main_ui.console_window.addItem(
                    f"Added {item_key} as {item_name} with index of {item_index}")

        else:
            QtWidgets.QMessageBox.critical(
                self, "CAUTION", "Automatic backup system is failed to backup.\nFurther generating scripts is cancelled")

    # start the whole system
    def gen_button_act(self):
        if self.wep_index and len(self.wep_name) and len(self.wep_indi) > 0:

            self.start_check()

            # action if all required file is checked and exist
            if self.f1_status == True and self.f2_status == True and self.f3_status == True:
                if BackupFiles(self.INDI_PATH, self.DICT_PATH, self.BACKUP_FILELIMIT).compress_succes:
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

    # checking wether input file is exist
    def check_file(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
            return False

    # GET INPUT VALUE FROM USER

    # get weapon index from user input
    def weapon_index_act(self, value):
        if len(value) > 0:
            self.wep_index = value
            self.wep_index = int(self.wep_index)
            print(self.wep_index)
        else:
            None

    # get weapon name from user input
    def weapon_name_act(self, value):
        if len(value) > 0:
            self.wep_name = value
            print(self.wep_name)
        else:
            None

    # get weapon indication from user input
    def weapon_indi_act(self, value):
        if len(value) > 0:
            self.wep_indi = value
            print(self.wep_indi)
        else:
            None

    # get starting batch set index from user input
    def get_index_start(self, value):
        if len(value) > 0:
            self.main_ui.start_batch.setDisabled(False)
            self.batchset_index = int(value)
            print(self.batchset_index)
        else:
            self.main_ui.start_batch.setDisabled(True)

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
