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

        self.init()
        print(self.name_items)
        print(self.key_items)

    # start the whole system
    def init(self):

        # self.find_file()

        if self.ACTIVE:
            print("file meet requirment")
            self.find_name()
            self.find_key()
        else:
            print("file not meet requirment")

    def find_name(self):
        for item in self.file_contents:
            item = item.replace('\n', '')
            # print(f"\n{item}")

            find_name = re.finditer(self.NAME_PATTERN, item)

            for item in find_name:
                item = item.group(0)

                for char in self.REMOVE_CHAR:
                    if char in item:
                        item = item.replace(char, '')

                self.name_items.append(item)
                print(item)

    # find indication key
    def find_key(self):
        for item in self.file_contents:
            item = item.replace('\n', '')
            # print(f"\n{item}")

            find_key = re.finditer(self.KEY_PATTERN, item)

            for item in find_key:
                item = item.group(0)

                for char in self.REMOVE_CHAR:
                    if char in item:
                        item = item.replace(char, '')
                self.key_items.append(item)
                print(item)


# x = BatchProcessing('batch\\batch-test.txt')
# print(x)
