import shutil
import fnmatch
import os
import re


class BatchProcessing:
    def __init__(self, file_contents, active):
        self.NAME_PATTERN = r'\[.*?\]'
        self.KEY_PATTERN = r'\(.*?\)'
        self.OPEN_MODE = 'r'
        self.REMOVE_CHAR = ["[", "]", "(", ")"]
        self.ACTIVE = active
        self.file_contents = file_contents
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
        for item in self.file_contents:
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
