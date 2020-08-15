import shutil
import fnmatch
import os
import re


class Batch:
    def __init__(self, path):
        self.current_dir = os.path.abspath(os.getcwd())
        self.path = path
        try:
            self.file = open(path, 'r+')
            self.err = False
        except FileNotFoundError as e:
            print("file not found")
            self.err = True
            raise e

    def activate_batch(self):
        """Mark opened text file as eligible batch set"""
        if not self.err:
            with open(self.path, 'r+') as f:
                contents = f.readlines()
                if self.is_active():
                    print("Batch set already activated")
                else:
                    try:
                        contents.remove("deactivate\n")
                    except ValueError as e:
                        pass
                    finally:
                        self.clear_content(f)
                        contents.insert(0, "activate\n")
                        contents = "".join(contents)
                        f.seek(0)
                        f.write(contents)

    def deactivate_batch(self):
        """Mark opened text file as deactivated batch set"""
        if not self.err:
            with open(self.path, 'r+') as f:
                contents = f.readlines()
                if not self.is_active():
                    print("Batch set already deactivated")
                else:
                    try:
                        contents.remove("activate\n")
                    except ValueError as e:
                        pass
                    finally:
                        self.clear_content(f)
                        contents.insert(0, "deactivate\n")
                        contents = "".join(contents)
                        f.seek(0)
                        f.write(contents)

    def get_items(self):
        """Get items from opened batch set"""
        items = dict()

        with open(self.path, 'r') as f:
            contents = f.readlines()

            for line in contents:

                m = re.search('\[(.+?)\]', line.strip())
                n = re.search('\((.+?)\)', line.strip())
                index = re.search('(--\d{1,4})', line.strip())

                if m and n and index:
                    temp = index.group(1)
                    temp = temp.replace('-', '')
                    items[n.group(1)] = [m.group(1), int(temp)]
                elif m and n:
                    items[n.group(1)] = m.group(1)

        return items

    def add_item(self, key, value):
        """Add item to opened batch set"""
        if isinstance(key, str) and isinstance(value, str):
            with open(self.path, "r+") as f:
                f.readlines()
                f.write(f"[{key}] ({value})")
        else:
            raise TypeError("Invalid input type, please use string")

    def gen_script(self, index=1):
        """Generate script from current opened batch set"""
        items = self.get_items()
        temp_index = index
        indexed_items = {}
        index_list = []

        # Get list of index for every batch item
        for name, indi in items.items():
            if not isinstance(indi, list):
                index_list.append(temp_index)
                temp_index += 1
            else:
                index_list.append(int(indi[1]))

        # Put batch item in dictionary with all the characteristic
        for (key, value), point in zip(items.items(), index_list):
            if not isinstance(value, list):
                indexed_items[point] = [key, value]
            else:
                indexed_items[point] = [key, value[0]]

        con_path = f'{self.current_dir}\\HUD\\HudSetup\\KillText\\'
        dict_path = f'{self.current_dir}\\game\\scoring_wpn.py'

        # Generating on con files section
        for i in sorted(indexed_items.keys()):
            for page in range(1, 7):
                try:
                    with open(f'{con_path}CustomizeIndication{page}Weapon.con', 'r+') as f:
                        string1 = f"""
hudBuilder.createPictureNode\t\tIngameHud Indication{page}weapon{i} 301 352 162 24
hudBuilder.setPictureNodeTexture\tIngame/Killtext/Indication/Indicationweapon{i}.dds
hudBuilder.setNodeShowVariable\t\tDemoRecInterfaceShow
hudBuilder.setNodeColor\t\t\t\t1 1 1 0.8
hudBuilder.setNodeInTime\t\t\t0.15
hudBuilder.setNodeOutTime\t\t\t0.2
hudBuilder.addNodeMoveShowEffect\t0 90
hudBuilder.addNodeAlphaShowEffect
hudBuilder.addNodeBlendEffect\t\t7 2
"""
                        f.readlines()
                        f.write(string1)

                except FileNotFoundError:
                    print(
                        f"Error while writing on '{con_path}CustomizeIndication{page}Weapon.con'.\nReason: File not exist")

            try:
                with open(f'{con_path}HudElementsAttackerWeapon.con', 'r+') as f:
                    string2 = f"""
hudBuilder.createPictureNode\t\tIngameHud AttackerWeapon{i} 378 496 216 32
hudBuilder.setPictureNodeTexture\tIngame/Killtext/KilledIndication/KilledIndicationWeapon{i}.dds
hudBuilder.setNodeShowVariable\t\tDemoRecInterfaceShow
hudBuilder.setNodeColor\t\t\t\t1 1 1 0.8
hudBuilder.setNodeInTime\t\t\t0.2
hudBuilder.setNodeOutTime\t\t\t0.1
hudBuilder.addNodeAlphaShowEffect
hudBuilder.addNodeBlendEffect\t\t7 2
"""
                    f.readlines()
                    f.write(string2)

            except FileNotFoundError:
                print(
                    f"Error while writing on '{con_path}HudElementsAttackerWeapon.con'.\nReason: File not exist")

            # index += 1

        # Generating on python dictionary section
        try:
            with open(dict_path, 'r+') as f:
                contents = f.readlines()
                index_dict = {}

                for num, line in enumerate(contents, 1):
                    item = re.search('(:.+?,)', line.strip())
                    if item:
                        conv_srch = item.group(1)
                        conv_srch = conv_srch.translate(
                            conv_srch.maketrans('', '', ':, '))
                        index_dict[int(conv_srch)] = num

                for (key, value), increment_index in zip(sorted(indexed_items.items()), range(len(indexed_items))):
                    if key in index_dict.keys():
                        contents.insert(index_dict.get(key)+increment_index,
                                        f"\t\t\"{value[0]}\"\t\t\t: {key},\t\t# {value[1]}\n")
                        increment_index += 1

                contents = "".join(contents)

                self.clear_content(f)
                f.write(contents)

                self.deactivate_batch()

        except FileNotFoundError as e:
            print("File cannot be found")

    def gen_texture(self):
        pass

    def is_active(self):
        """Check if opened text file if it's active or not"""
        if not self.err:
            with open(self.path, 'r') as f:
                contents = f.readlines()
                contents = [item.replace('\n', '') for item in contents]
                if contents.count("deactivate".casefold()) > 0:
                    return False
                elif contents.count("activate".casefold()) > 0:
                    return True
                else:
                    return False

    def clear_content(self, del_content):
        """Clear the contents of current opened file"""
        del_content.read().split('\n')
        del_content.seek(0)
        del_content.truncate()


x = Batch(
    "D:\\Documents\\GitHub\\BF2Dynamic-Indication-Generator\\batch\\batch-test.txt")
x.gen_script(4)
# test = {1: 2, 3: 4}
# test[1] = [5]
# print(test)


class BatchProcessing:
    def __init__(self, file_contents, active):
        self.NAME_PATTERN = r'\[.*?\]'
        self.KEY_PATTERN = r'\(.*?\)'
        self.OPEN_MODE = 'r'
        self.REMOVE_CHAR = ["[", "]", "(", ")"]
        self.ACTIVE = active
        self.FILE_CONTENTS = file_contents
        self.file_exist = bool()
        self.name_items = list()
        self.key_items = list()
        self.items = list()

        self.init()

    # start the whole system
    def init(self):

        if self.ACTIVE:
            print("file meet requirment")
            self.find_item()
            self.find_name()
            self.find_key()
        else:
            print("file not meet requirment")

    # find a valid item
    def find_item(self):
        for item in self.FILE_CONTENTS:
            item = item.replace('\n', '')

            find_item = re.finditer(
                f'{self.NAME_PATTERN} {self.KEY_PATTERN}', item)

            for item in find_item:
                item = item.group(0)

                self.items.append(item)
                print(item)

    # find name from scanned valid item
    def find_name(self):
        for item in self.items:

            find_name = re.finditer(self.NAME_PATTERN, item)

            for item in find_name:
                item = item.group(0)

                for char in self.REMOVE_CHAR:
                    if char in item:
                        item = item.replace(char, '')

                self.name_items.append(item)
                print(item)

    # find indication key from scanned valid item
    def find_key(self):
        for item in self.items:

            find_key = re.finditer(self.KEY_PATTERN, item)

            for item in find_key:
                item = item.group(0)

                for char in self.REMOVE_CHAR:
                    if char in item:
                        item = item.replace(char, '')
                self.key_items.append(item)
                print(item)
