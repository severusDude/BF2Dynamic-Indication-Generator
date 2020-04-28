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
            self.check_files()
        else:
            self.wep_index = 161
            self.wep_name = "USRIF_M4"
            self.wep_indi = "M4"
            self.check_files()
            # QtWidgets.QMessageBox.warning(
            #     self, "Error", "You need to input all the textfield")

    def check_files(self):
        for page in range(1, 7):
            self.indi1_act(self.wep_index, page)

    def indi1_act(self, index, file_index):
        try:
            with open(f'HUD\\HudSetup\\Killtext\\HudElementsIndication{file_index}.con', 'r+') as f:
                print(f.readlines())
                self.write_indi(f, file_index, index)

        except FileNotFoundError as e:
            print(f"Required file not exist {e}")
            return False
        finally:
            f.close()

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
