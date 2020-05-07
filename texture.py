from win32com.client import Dispatch
import pathlib
import os

APP = "Photoshop.Application"
EXPORT_AS = "Photoshop.ExportOptionsSaveForWeb"

CURRENT_DIR = str(pathlib.Path(__file__).parent.absolute())

print(CURRENT_DIR)

if not os.path.exists(f"{CURRENT_DIR}\\export"):
    os.makedirs(f"{CURRENT_DIR}\\export")

INDI_PATH = f"psd\\Indicationweapon.psd"
KILLED_PATH = f"psd\\KilledIndicationWeapon.psd"

PSAPP = Dispatch(APP)

OPTIONS = Dispatch(EXPORT_AS)
OPTIONS.Format = 13
OPTIONS.PNG8 = False


class GenerateTextureSingle:
    def __init__(self, index, indi):
        self.INDEX = index
        self.INDI = indi

        self.open_psd("indi")
        # self.open_psd("killed")

    def open_psd(self, filename):
        if filename == "indi":
            PSAPP.Open(f"{CURRENT_DIR}\\{INDI_PATH}")
            doc = PSAPP.Application.ActiveDocument
            self.generate_indi(doc)

        elif filename == "killed":
            PSAPP.Open(f"{CURRENT_DIR}\\{KILLED_PATH}")
            doc = PSAPP.Application.ActiveDocument
            self.generate_killed(doc)

        else:
            print("unknown keyword")

    def generate_indi(self, doc):
        shade = doc.ArtLayers["Shade"]
        main = doc.ArtLayers["Main"]

        shade_text = shade.TextItem
        main_text = main.TextItem

        shade_text.contents = f"[{self.INDI.upper()}]"
        main_text.contents = f"[{self.INDI.upper()}]"

        export_png = f"{CURRENT_DIR}\\export\\Indicationweapon{self.INDEX}.png"

        doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

    def generate_killed(self, doc):
        pass


class GenerateTextureBatch:
    def __init__(self, wep_list, index):
        self.WEP_LIST = wep_list
        self.INDEX = index
        self.LAST_INDEX = len(self.WEP_LIST) + self.INDEX

        self.open_psd("indi")
        self.open_psd("killed")

    def open_psd(self, filename):
        if filename == "indi":
            PSAPP.Open(f"{CURRENT_DIR}\\{INDI_PATH}")
            doc = PSAPP.Application.ActiveDocument
            self.generate_indi(doc)

        elif filename == "killed":
            PSAPP.Open(f"{CURRENT_DIR}\\{KILLED_PATH}")
            doc = PSAPP.Application.ActiveDocument
            self.generate_killed(doc)

        else:
            print("unknown keyword")

    def generate_indi(self, doc):
        for fileindex, item in zip(range(self.INDEX, self.LAST_INDEX), self.WEP_LIST):
            shade = doc.ArtLayers["Shade"]
            main = doc.ArtLayers["Main"]

            shade_text = shade.TextItem
            main_text = main.TextItem

            shade_text.contents = f"[{item.upper()}]"
            main_text.contents = f"[{item.upper()}]"

            export_png = f"{CURRENT_DIR}\\export\\Indicationweapon{fileindex}.png"

            doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

    def generate_killed(self, doc):
        pass
