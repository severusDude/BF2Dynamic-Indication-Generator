import os

from win32com.client import Dispatch
from wand.image import Image
from psd_tools import PSDImage

APP = "Photoshop.Application"
EXPORT_AS = "Photoshop.ExportOptionsSaveForWeb"

# paths
CURRENT_DIR = str(os.path.abspath(os.getcwd()))
EXPORT_PATH = f"{CURRENT_DIR}\\export"
PNG_PATH = f"{CURRENT_DIR}\\export\\png"
DDS_PATH = f"{CURRENT_DIR}\\export\\dds"

if not os.path.exists(EXPORT_PATH):
    os.makedirs(EXPORT_PATH)
    if not os.path.exists(PNG_PATH):
        os.makedirs(PNG_PATH)
        if not os.path.exists(f"{PNG_PATH}\\Indication"):
            os.makedirs(f"{PNG_PATH}\\Indication")
        if not os.path.exists(f"{PNG_PATH}\\KilledIndication"):
            os.makedirs(f"{PNG_PATH}\\KilledIndication")
    if not os.path.exists(DDS_PATH):
        os.makedirs(DDS_PATH)
        if not os.path.exists(f"{DDS_PATH}\\Indication"):
            os.makedirs(f"{DDS_PATH}\\Indication")
        if not os.path.exists(f"{DDS_PATH}\\KilledIndication"):
            os.makedirs(f"{DDS_PATH}\\KilledIndication")

INDI_PATH = f"{CURRENT_DIR}\\psd\\Indicationweapon.psd"
KILLED_PATH = f"{CURRENT_DIR}\\psd\\KilledIndicationWeapon.psd"

PSAPP = Dispatch(APP)

OPTIONS = Dispatch(EXPORT_AS)
OPTIONS.Format = 13
OPTIONS.PNG8 = False


class GenerateTexture:

    @staticmethod
    def init_killindi(index, indi, filepath=INDI_PATH):
        PSAPP.Open(filepath)
        doc = PSAPP.Application.ActiveDocument

        STRING = f"[{indi.upper()}]"

        shade = doc.ArtLayers["Shade"]
        main = doc.ArtLayers["Main"]

        shade_text = shade.TextItem
        main_text = main.TextItem

        shade_text.contents = STRING
        main_text.contents = STRING

        export_png = f"{PNG_PATH}\\Indication\\Indicationweapon{index}.png"
        export_dds = f"{DDS_PATH}\\Indication\\Indicationweapon{index}.dds"

        doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

        with Image(filename=export_png) as img:
            img.compression = 'dxt5'
            img.save(filename=export_dds)

    @staticmethod
    def init_killedindi(index, indi, filepath=KILLED_PATH):
        PSAPP.Open(filepath)
        doc = PSAPP.Application.ActiveDocument

        STRING = f"[{indi.upper()}]"
        DISTANCE = 12

        shade = doc.ArtLayers["Shade"]
        main = doc.ArtLayers["Main"]

        shade_text = shade.TextItem
        main_text = main.TextItem

        shade_text.contents = STRING
        main_text.contents = STRING

        doc.save
        doc.close

        reposition = PSDImage.open(filepath)

        for main in reposition.descendants():
            if main.name == "Main":
                left_coord = main.left
                main_width = main.width

        rel_pos = left_coord + main_width + DISTANCE
        for layer in reposition.descendants():
            if layer.name == "YOU":
                if layer.left != rel_pos:
                    layer.left = rel_pos

        reposition.save

        export_png = f"{PNG_PATH}\\KilledIndication\\KilledIndicationWeapon{index}.png"
        export_dds = f"{DDS_PATH}\\KilledIndication\\KilledIndicationWeapon{index}.dds"

        PSAPP.Open(filepath)
        reopen_doc = PSAPP.Application.ActiveDocument

        reopen_doc.Export(ExportIn=export_png, ExportAs=2, Options=OPTIONS)

        with Image(filename=export_png) as img:
            img.compression = 'dxt5'
            img.save(filename=export_dds)

    @staticmethod
    def init_name(index, name, filepath):
        pass

    @staticmethod
    def init_dogtag(index, name, filepath):
        pass
