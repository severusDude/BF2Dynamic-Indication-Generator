from PyQt5 import QtCore, QtGui, QtWidgets
from Generate import *
import qdarkstyle
import sys


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = UserInterface()
        self.main_ui.setupUi(self)
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
        # self.main_ui.gen_button.setDisabled(True)

    def gen_button_act(self):
        if self.wep_index and len(self.wep_name) and len(self.wep_indi) > 0:
            self.weapon_dict_manage(
                self.wep_index, self.wep_name, self.wep_indi)
            # self.check_files()
        else:
            self.wep_index = 161
            self.wep_name = "USRIF_M4"
            self.wep_indi = "M4"
            self.weapon_dict_manage(
                self.wep_index, self.wep_name, self.wep_indi)
            # self.check_files()
            # QtWidgets.QMessageBox.warning(
            #     self, "Error", "You need to input all the textfield")

    def weapon_dict_manage(self, index, name, indi):
        try:
            with open('game\\weapons.py', 'r+') as f:
                # print(f.readlines())
                x = self.weapon_dict_add(f, index, name, indi)
                f.write(x)
        except FileNotFoundError as e:
            print(f"Required dictionary doesn't exist {e}")
        finally:
            f.close()

    def weapon_dict_add(self, file, index, name, indi):
        contents = file.readlines()
        text_line, req_index = self.find_dict_place(contents, index)
        print(text_line)
        x = self.line_num_for_phrase_in_file(text_line, file)
        print(x)

        req_index = int(req_index)
        contents.insert(req_index,
                        f"		\"{name}\"			 : {index},		 # {indi}")
        contents = "".join(contents)
        return contents

    def find_dict_place(self, file, index):
        for num, line in enumerate(file, 1):
            index_str = index - 1
            index_str = str(index_str)
            if index_str in line:
                print(f"it here {index_str}")
                return line, index_str

    def line_num_for_phrase_in_file(self, phrase, file):
        if phrase in file:
            x = file.index(phrase)
            return x

        return -1
        # for (i, line) in enumerate(file, 1):
        #     if phrase in line:
        #         return i
        # return -1

        # loop indication call based on page index
    def check_files(self):
        for page in range(1, 7):
            self.indi_act(self.wep_index, page)

    # control to open, close and write indication
    def indi_act(self, index, file_index):
        try:
            with open(f'HUD\\HudSetup\\Killtext\\HudElementsIndication{file_index}.con', 'r+') as f:
                self.write_indi(f, file_index, index)

        except FileNotFoundError as e:
            print(f"Required file not exist {e}")
            return False
        finally:
            f.close()

    # write indication based on page index and weapon index
    def write_indi(self, file, indi_page, indi_index):
        string = f"hudBuilder.createPictureNode\tIngameHud Indication{indi_page}weapon{indi_index} 270 352 216 32\nhudBuilder.setPictureNodeTexture \tIngame/Killtext/Indication/Indicationweapon{indi_index}.dds\nhudBuilder.setNodeShowVariable\tDemoRecInterfaceShow\nhudBuilder.setNodeColor\t\t1 1 1 0.8\nhudBuilder.setNodeInTime\t0.15\nhudBuilder.setNodeOutTime\t0.2\nhudBuilder.addNodeMoveShowEffect\t0 90\nhudBuilder.addNodeAlphaShowEffect\nhudBuilder.addNodeBlendEffect\t\t7 2\n\n"
        file.write(string)
        return True

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
