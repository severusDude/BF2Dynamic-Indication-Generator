import os

from win32com.client import Dispatch
from wand.image import Image
import psd_tools

APP = "Photoshop.Application"
EXPORT_AS = "Photoshop.ExportOptionsSaveForWeb"

# path
CURRENT_DIR = str(os.path.abspath(os.getcwd()))
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


class GenerateTexture:
    def __init__(self, index, indi):
        self.INDEX = index
        self.INDI = indi

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
        shade = doc.ArtLayers["Shade"]
        main = doc.ArtLayers["Main"]

        shade_text = shade.TextItem
        main_text = main.TextItem

        shade_text.contents = f"[{self.INDI.upper()}]"
        main_text.contents = f"[{self.INDI.upper()}]"

        doc.save
        doc.close

        reposition = psd_tools.PSDImage.open(f"{CURRENT_DIR}\\{KILLED_PATH}")

        for main in reposition.descendants():
            if main.name == "Main":
                main_left = main.left
                main_width = main.width

        rel_pos = main_left + main_width + 12
        for layer in reposition.descendants():
            if layer.name == "YOU":
                if layer.left != rel_pos:
                    layer.left = rel_pos

        print(rel_pos)
        reposition.save(f'{CURRENT_DIR}\\{KILLED_PATH}')

        export_png = f"{CURRENT_DIR}\\export\\png\\KilledIndicationWeapon{self.INDEX}.png"
        export_dds = f"{CURRENT_DIR}\\export\\dds\\KilledIndicationWeapon{self.INDEX}.dds"

        PSAPP.Open(f"{CURRENT_DIR}\\{KILLED_PATH}")
        reopen_doc = PSAPP.Application.ActiveDocument

        reopen_doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

        with Image(filename=export_png) as img:
            img.compression = 'dxt5'
            img.save(filename=export_dds)
