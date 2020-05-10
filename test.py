import os

from PyQt5 import QtCore, QtGui, QtWidgets
import psd_tools
from psd_tools.api.layers import Layer
import win32com.client


class Test:
    def __init__(self):
        self.INDI_PATH = 'HUD\\HudSetup\\KillText'
        self.DICT_PATH = 'game'
        self.INDEX_START = 1
        self.INDEX_END = 7

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

    def check_file(self, filepath):
        if os.path.exists(filepath):
            return True
        else:
            return False


class Test1:
    def __init__(self):
        self.CURRENT_DIR = os.path.abspath(os.getcwd())
        self.INDI_PATH = f'{self.CURRENT_DIR}\\psd\\Indicationweapon.psd'
        self.KILLED_PATH = f'{self.CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd'
        self.LEFT_ALIGN = 101
        self.TEXT_ALIGN_YOU = 806
        self.RIGHT_ALIGN_YOU = 12

        self.generate()

    def generate(self):
        # with PSDImage.open(self.INDI_PATH) as indi_doc:
        #     for layer in indi_doc.:

        indi_doc = psd_tools.PSDImage.open(self.KILLED_PATH)

        for layer in indi_doc.descendants():

            if layer.name == "Shade":
                shade = layer
                shade_left = layer.left
                shade_right = layer.right
                shade_width = layer.width

                if layer.left != self.LEFT_ALIGN:
                    layer.left = self.LEFT_ALIGN

            if layer.name == "Main":
                main = layer
                main_left = layer.left
                main_right = layer.right
                main_width = layer.width

                if layer.left != self.LEFT_ALIGN:
                    layer.left = self.LEFT_ALIGN

        print(f"{main_width}")

        for layer2 in indi_doc.descendants():

            if layer2.name == "YOU":
                you = layer2
                you_left = layer2.left
                you_loc = main_left + main_width + 12

                if layer2.left != you_loc:
                    layer2.left = you_loc

        indi_doc.save('try1.psd')

        # print(f"difference is {main_left} {you_left} {you_left - main_left}")


x = Test1()

# 159
# left align text layers with patch layer
# align text
