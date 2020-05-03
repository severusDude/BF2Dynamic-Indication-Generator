from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


class DuplicateBatchSafety:
    def __init__(self, filepath, open_mode):
        self.FILEPATH = filepath
        self.OPEN_MODE = open_mode
        self.DEACTIVATE_KEY = "deactivate"
        self.ACTIVATED_KEY = "activate"

        self.init()

    def init(self):
        self.read_batchset()

    def read_batchset(self):
        with open(self.FILEPATH, self.OPEN_MODE) as f:
            self.deactivate_batchset(f)

    def deactivate_batchset(self, file):
        self.contents = file.readlines()

        read = open(self.FILEPATH, 'r')

        if self.contents[0] == f"{self.ACTIVATED_KEY}\n":
            new_file_content = ""
            for line in read:
                stripped_line = line.strip()
                new_line = stripped_line.replace(
                    self.ACTIVATED_KEY, self.DEACTIVATE_KEY)
                new_file_content += new_line + "\n"
            read.close()

            with open(self.FILEPATH, 'w') as write:
                write.write(new_file_content)

        elif self.contents[0] == f"{self.DEACTIVATE_KEY}\n":
            print("File already deactivated")
        else:
            unknown_key = self.contents[0]
            print(f"Error: {unknown_key}Is an unknown key")


x = DuplicateBatchSafety('batch\\batch-test.txt', 'r+')
