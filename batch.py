import shutil
import fnmatch
import os
import re


class BatchProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_exist = bool()
        self.is_active = bool()
        self.contents = list()
        self.name_bracket = r'\[.*?\]'
        self.file_bracket = r'\(.*?\)'
        self.open_mode = 'r'
        self.activation_key = "activate"

        self.init()

    def init(self):

        self.find_file()

        if self.file_exist:
            print("succes, file is exist")
            if self.is_active:
                print("file meet requirment")
                self.find_name()
            else:
                print("file not meet requirment")

        else:
            print("failed, file not exist")

    def find_file(self):
        if os.path.exists(self.file_path):
            self.file_exist = True

            with open(self.file_path, self.open_mode) as f:
                self.check_file(f.readlines())

        else:
            self.file_exist = False

    def check_file(self, contents):
        print(contents)
        self.contents = contents
        key = self.contents[0]
        key = key.replace('\n', '')

        if key == self.activation_key:
            self.is_active = True
            print("batch file is active")

        else:
            self.is_active = False
            print("batch file is passive")

    def find_name(self):
        for item in self.contents:
            item = item.replace('\n', '')
            print(f"\n{item}")

            find_name = re.finditer(r'\[.*?\]', item)

            for item in find_name:
                print(item)


text = """
[SCAR SV] (bf4_scar_sv)
[ACR] (bf4_acr)
"""

output_file = re.finditer(r'\[.*?\]', text)
req_file = re.finditer(r'\(.*?\)', text)
for output_filename in output_file:
    print(output_filename)

for req_filename in req_file:
    print(req_filename)

x = BatchProcessing('batch\\batch-test.txt')
print(x)
