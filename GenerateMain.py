import sys
import os
import webbrowser
import pkg_resources.py2_warn

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

from Generate import *
from backup import *
from batch import *
from batchSafety import *
from generateindication import *
from generatedictionary import *
from texture import *


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
        self.batch_contents = str()
        self.is_active = bool()
        self.gen_texture1 = bool()
        self.gen_texture2 = bool()
        self.gen_script1 = True
        self.gen_script2 = True
        self.index_filled = bool()
        self.CURRENT_DIR = str(os.path.abspath(os.getcwd()))
        self.EXPORT_ROOT = f'{self.CURRENT_DIR}\\export'
        self.EXPORT_PNG = f'{self.CURRENT_DIR}\\export\\png'
        self.EXPORT_DDS = f'{self.CURRENT_DIR}\\export\\dds'
        self.BATCHSET_PATH = str()
        self.OPTION_1 = "SINGLE GENERATE"
        self.OPTION_2 = "BATCH PROCESSING"
        self.OPEN_MODE = 'r'
        self.BACKUP_PATH = 'backups'
        self.INDI_PATH = 'HUD\\HudSetup\\KillText'
        self.DICT_PATH = 'game'
        self.ACTIVATION_KEY = "activate"
        self.DEACTIVATION_KEY = "deactivate"
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
        self.main_ui.choose_batchfile.clicked.connect(self.open_batchfile)

        # start batch from opened batch set
        self.main_ui.start_batch.clicked.connect(self.start_batch)

        # batch processing guide
        self.main_ui.batch_guide.clicked.connect(
            lambda: webbrowser.open_new_tab('https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md#create-batch-set-file'))

        self.main_ui.gen_texture1.stateChanged.connect(self.gen1_picker1)
        self.main_ui.gen_texture2.stateChanged.connect(self.gen1_picker2)

        self.main_ui.gen_script1.stateChanged.connect(self.gen2_picker1)
        self.main_ui.gen_script2.stateChanged.connect(self.gen2_picker2)

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
    def open_batchfile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open batch file", "", "*.txt", options=options)

        if filename:

            self.BATCHSET_PATH = filename

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
            self.main_ui.batch_active.setText("Batch set is active")
            self.main_ui.batch_active.adjustSize()

            self.main_ui.start_batch.setDisabled(False)

        elif key == self.DEACTIVATION_KEY:

            self.is_active = False
            self.main_ui.batch_active.setText(
                "Batch set is deactivated,\nTo reactivate, see guide")
            self.main_ui.batch_active.adjustSize()
            self.main_ui.start_batch.setDisabled(True)

        else:
            self.is_active = False
            self.main_ui.batch_active.setText(
                "Batch file is not active,\nplease see guide to make your own batch set")
            self.main_ui.batch_active.adjustSize()

            self.main_ui.start_batch.setDisabled(True)

    def batch_active(self):

        self.main_ui.index_start.setDisabled(False)
        self.main_ui.index_label.setDisabled(False)

        self.main_ui.gen_texture2.setDisabled(False)
        self.main_ui.texture_label2.setDisabled(False)

        self.main_ui.gen_script2.setDisabled(False)
        self.main_ui.script_label2.setDisabled(False)

        self.batchset_items = BatchProcessing(
            self.batch_contents, self.is_active)

        self.main_ui.console_window.addItem(
            f"Found {len(self.batchset_items.items)} valid items from batch set:")

        for item in self.batchset_items.items:
            self.main_ui.console_window.addItem(f"    {item}")

    def start_batch(self):

        if self.check_files():

            if self.batchset_index > 0:

                # re read batch if there's any changes
                with open(self.BATCHSET_PATH, self.OPEN_MODE) as f:
                    re_readbatch = f.readlines()

                # get item criteria
                item_count = len(self.batchset_items.items)
                last_index = self.batchset_index + item_count
                name_list = self.batchset_items.name_items
                key_list = self.batchset_items.key_items

                if BackupFiles(self.INDI_PATH, self.DICT_PATH, self.BACKUP_FILELIMIT).compress_succes:

                    if re_readbatch[0] == f"{self.DEACTIVATION_KEY}\n":
                        QtWidgets.QMessageBox.warning(
                            self, "Batch Processing Failed", "Error occur when trying to batch processing\nReason: batch set is deactivated")

                    elif re_readbatch[0] == f"{self.ACTIVATION_KEY}\n":

                        if self.gen_script2:
                            # deactivate batch set
                            DuplicateBatchSafety(
                                self.BATCHSET_PATH)

                            # generate indication from batch set
                            for item in range(self.batchset_index, last_index):
                                self.gen_indi.init(item)
                                self.main_ui.console_window.addItem(
                                    f"Added index {item} into Indication Files")

                            for item_name, item_key, item_index in zip(name_list, key_list, range(self.batchset_index, last_index)):
                                self.gen_dict.init(
                                    item_key, item_index, item_name)
                                self.main_ui.console_window.addItem(
                                    f"Added {item_key} as {item_name} with index of {item_index}")

                            QtWidgets.QMessageBox.information(
                                self, "Batch Processing Succesfull", "Batch processing is succesfull\nBatch set is now deactivated,\nplease re-examine the files before you moved them to your mod\n\nScript is generated")

                        if self.gen_texture2:
                            if self.check_file(f"{self.CURRENT_DIR}\\psd\\Indicationweapon.psd"):
                                if self.check_file(f"{self.CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd"):
                                    self.check_exportroot()
                                    # deactivate batch set
                                    DuplicateBatchSafety(
                                        self.BATCHSET_PATH)

                                    for tex_name, tex_index in zip(name_list, range(self.batchset_index, last_index)):
                                        GenerateTexture(
                                            tex_index, tex_name)
                                        self.main_ui.console_window.addItem(
                                            f"Texture index {tex_index} is generated with text {tex_name}")

                                    QtWidgets.QMessageBox.information(
                                        self, "Batch Processing Succesfull", "Batch Processing is succesfull\nBatch set is now deactivated,\nplease re-examine the files before you moved them to your mod\n\nTexture is generated")

                                else:
                                    QtWidgets.QMessageBox.warning(
                                        self, "Error FNE_PSD_2", f"Error code: PSD_2\n\nRequired file missing\n\t{self.CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd")

                            else:
                                QtWidgets.QMessageBox.warning(
                                    self, "Error FNE_PSD_1", f"Error code: PSD_1\n\nRequired file missing\n\t{self.CURRENT_DIR}\\psd\\Indicationweapon.psd")

                        if self.gen_script2 == False and self.gen_texture2 == False:
                            QtWidgets.QMessageBox.warning(
                                self, "Error", "You must select atleast one of the options")

                        self.main_ui.batch_active.setText(
                            "Batch set is deactivated,\nTo reactivate, see guide")
                        self.main_ui.batch_active.adjustSize()

                    else:
                        QtWidgets.QMessageBox.warning(
                            self, "Batch Processing Failed", "Error occur when trying to batch processing\nReason: batch set have unknown key activation")

                else:
                    QtWidgets.QMessageBox.critical(
                        self, "CAUTION", "Automatic backup system is failed to backup.\nFurther generating scripts is cancelled")

            else:
                QtWidgets.QMessageBox.warning(
                    self, "Error EI_2", "Batch index start is have not been inputted")

        else:
            QtWidgets.QMessageBox.warning(
                self, "Error FNE" "Required file missing, further generating is cancelled")

    # start the whole system
    def gen_button_act(self):
        if self.wep_index > 0 and len(self.wep_name) > 0 and len(self.wep_indi) > 0:

            if self.check_files():

                if BackupFiles(self.INDI_PATH, self.DICT_PATH, self.BACKUP_FILELIMIT).compress_succes:

                    if self.gen_script1:
                        self.gen_indi.init(self.wep_index)
                        self.gen_dict.init(
                            self.wep_name, self.wep_index, self.wep_indi)

                        QtWidgets.QMessageBox.information(
                            self, "Succes", "Succes generating scripts\nPlease re-check the files to make sure eveything was done correctly\n\nScripts are generated")

                    if self.gen_texture1:
                        if self.check_file(f"{CURRENT_DIR}\\psd\\Indicationweapon.psd"):
                            if self.check_file(f"{CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd"):
                                self.check_exportroot()

                                GenerateTexture(
                                    self.wep_index, self.wep_indi)

                                QtWidgets.QMessageBox.information(
                                    self, "Succes", "Succes generating Texture\nPlease re-check the files to make sure everything was done correctly\n\nTexture is generated")

                            else:
                                QtWidgets.QMessageBox.warning(
                                    self, "Error FNE_PSD_2", f"Error code: PSD_2\n\nRequired file missing\n\t{self.CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd")

                        else:
                            QtWidgets.QMessageBox.warning(
                                self, "Error FNE_PSD_1", f"Error code: PSD_1\n\nRequired file missing\n\t{self.CURRENT_DIR}\\psd\\Indicationweapon.psd")

                    if self.gen_script1 == False and self.gen_texture1 == False:
                        QtWidgets.QMessageBox.warning(
                            self, "Error", "You must select atleast one of the options")

                else:
                    QtWidgets.QMessageBox.critical(
                        self, "CAUTION", "Automatic backup system is failed to backup.\nFurther generating scripts is cancelled")
                print("not ready")

            else:
                QtWidgets.QMessageBox.warning(
                    self, "Error FNE" "Required file missing, further generating is cancelled")

        else:
            QtWidgets.QMessageBox.warning(
                self, "Error EI_1", "You need to input all the textfield")

    # check required files is exist
    def check_files(self):

        # file statuses
        file1 = bool()
        file2 = bool()
        file3 = bool()

        # required files location
        att_con = f'{self.INDI_PATH}\\HudElementsAttackerWeapon.con'
        scor_wep = f'{self.DICT_PATH}\\scoring_wpn.py'

        # temporary variable to check 6 files of CustomizeIndicationWeapon.con
        page_list = list()
        page_listed = [temp for temp in range(
            self.INDEX_START, self.INDEX_END)]

        try:
            # check CustomizeIndication1-6Weapon.con files
            for page in range(self.INDEX_START, self.INDEX_END):
                cust_con = f'{self.INDI_PATH}\\CustomizeIndication{page}Weapon.con'
                if self.check_file(cust_con):
                    page_list.append(page)
                else:
                    print(
                        f"Error at CustomizeIndication{page}.con\nFile not found")
                    QtWidgets.QMessageBox.warning(
                        self, f"Error FNE_A_{page}", f"Error code: FNE_A_{page}\n\nRequired file is missing:\n\t{cust_con}")

            if page_list == page_listed:
                file1 = True

                # check AttackerWeapon.con
                if self.check_file(att_con):
                    file2 = True

                    # check scoring_wpn.py
                    if self.check_file(scor_wep):
                        file3 = True
                    else:
                        file3 = False
                        QtWidgets.QMessageBox.warning(
                            self, f"Error FNE_C", f"Error code: FNE_C\n\nRequired file is missing\n\t{scor_wep}")
                else:
                    file2 = False
                    QtWidgets.QMessageBox.warning(
                        self, f"Error FNE_B" f"Error code: FNE_B\n\nRequired file is missing:\n\t{att_con}")
            else:
                file1 = False

            if file1 == True and file2 == True and file3 == True:
                return True

        except:
            return False

    # checking if file is exist
    def check_file(self, filepath):
        if os.path.exists(filepath):
            return True
        else:
            return False

    def check_exportroot(self):
        if not os.path.exists(self.EXPORT_ROOT):
            os.makedirs(self.EXPORT_ROOT)
            if not os.path.exists(self.EXPORT_PNG):
                os.makedirs(self.EXPORT_PNG)
                if not os.path.exists(f"{self.EXPORT_PNG}\\Indication"):
                    os.makedirs(f"{self.EXPORT_PNG}\\Indication")
                if not os.path.exists(f"{self.EXPORT_PNG}\\KilledIndication"):
                    os.makedirs(f"{self.EXPORT_PNG}\\KilledIndication")
            if not os.path.exists(self.EXPORT_DDS):
                os.makedirs(self.EXPORT_DDS)
                if not os.path.exists(f"{self.EXPORT_DDS}\\Indication"):
                    os.makedirs(f"{self.EXPORT_DDS}\\Indication")
                if not os.path.exists(f"{self.EXPORT_DDS}\\KilledIndication"):
                    os.makedirs(f"{self.EXPORT_DDS}\\KilledIndication")

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
            self.index_filled = True
            self.batchset_index = int(value)
            print(self.batchset_index)
        else:
            self.index_filled = False

    # get state of single page check box
    def gen1_picker1(self, state):
        if state == QtCore.Qt.Checked:
            self.gen_texture1 = True
        else:
            self.gen_texture1 = False

    # get state of batch page check box
    def gen1_picker2(self, state):
        if state == QtCore.Qt.Checked:
            self.gen_texture2 = True
        else:
            self.gen_texture2 = False

    def gen2_picker1(self, state):
        if state == QtCore.Qt.Checked:
            print("generate script")
            self.gen_script1 = True
        else:
            self.gen_script1 = False

    def gen2_picker2(self, state):
        if state == QtCore.Qt.Checked:
            print("generate script")
            self.gen_script2 = True
        else:
            self.gen_script2 = False

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
