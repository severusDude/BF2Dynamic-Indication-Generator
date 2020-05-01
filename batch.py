import shutil
import fnmatch
import os
import re


class BatchProcessing:
    def __init__(self, file_path):
        self.FILE_PATH = file_path
        self.NAME_PATTERN = r'\[.*?\]'
        self.KEY_PATTERN = r'\(.*?\)'
        self.OPEN_MODE = 'r'
        self.ACTIVATION_KEY = "activate"
        self.REMOVE_CHAR = ["[", "]", "(", ")"]
        self.file_exist = bool()
        self.is_active = bool()
        self.file_contents = list()
        self.name_items = list()
        self.key_items = list()

        self.init()
        print(self.name_items)
        print(self.key_items)

    # start the whole system
    def init(self):

        self.find_file()

        if self.file_exist:
            print("succes, file is exist")
            if self.is_active:
                print("file meet requirment")
                self.find_name()
                self.find_key()
            else:
                print("file not meet requirment")

        else:
            print("failed, file not exist")

    # check the inputed file was exist
    def find_file(self):
        if os.path.exists(self.FILE_PATH):
            self.file_exist = True

            with open(self.FILE_PATH, self.OPEN_MODE) as f:
                self.check_file(f.readlines())

        else:
            self.file_exist = False

    # check if file meet requirments
    def check_file(self, contents):
        print(contents)
        self.file_contents = contents
        key = self.file_contents[0]
        key = key.replace('\n', '')
        print(self.file_contents)

        if key == self.ACTIVATION_KEY:
            self.is_active = True
            print("batch file is active")

        else:
            self.is_active = False
            print("batch file is passive")

    # find indication name
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


x = BatchProcessing('batch\\batch-test.txt')
print(x)
