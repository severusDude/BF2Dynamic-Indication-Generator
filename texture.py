import pathlib
import os

from win32com.client import Dispatch
from wand.image import Image

APP = "Photoshop.Application"
EXPORT_AS = "Photoshop.ExportOptionsSaveForWeb"

# path
CURRENT_DIR = str(pathlib.Path(__file__).parent.absolute())
EXPORT_PATH = f"{CURRENT_DIR}\\export"
PNG_PATH = f"{CURRENT_DIR}\\export\\png"
DDS_PATH = f"{CURRENT_DIR}\\export\\dds"

if not os.path.exists(EXPORT_PATH):
    os.makedirs(EXPORT_PATH)
    if not os.path.exists(PNG_PATH):
        os.makedirs(PNG_PATH)
    if not os.path.exists(DDS_PATH):
        os.makedirs(DDS_PATH)

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

        export_png = f"{CURRENT_DIR}\\export\\png\\Indicationweapon{self.INDEX}.png"
        export_dds = f"{CURRENT_DIR}\\export\\dds\\Indicationweapon{self.INDEX}.dds"

        doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

        with Image(filename=export_png) as img:
            img.compression = 'dxt5'
            img.save(filename=export_dds)

    def generate_killed(self, doc):
        pass


class GenerateTextureBatch:
    def __init__(self, index, wep_list):
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

            export_png = f"{CURRENT_DIR}\\export\\png\\Indicationweapon{fileindex}.png"
            export_dds = f"{CURRENT_DIR}\\export\\dds\\Indicationweapon{fileindex}.dds"

            doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

            with Image(filename=export_png) as img:
                img.compression = 'dxt5'
                img.save(filename=export_dds)

    def generate_killed(self, doc):
        pass
