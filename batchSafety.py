from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


class DuplicateBatchSafety:
    def __init__(self, filepath):
        self.FILEPATH = filepath
        self.OPEN_MODE = 'r+'
        self.DEACTIVATE_KEY = "deactivate"
        self.ACTIVATED_KEY = "activate"
        self.status = bool()

        self.init()

    # start system
    def init(self):
        self.read_batchset()

    # open batch set
    def read_batchset(self):
        with open(self.FILEPATH, self.OPEN_MODE) as f:
            self.deactivate_batchset(f)

    # deactivate opened batch set
    def deactivate_batchset(self, file):
        self.contents = file.readlines()

        read_file = open(self.FILEPATH, self.OPEN_MODE)

        if self.contents[0] == f"{self.ACTIVATED_KEY}\n":
            new_file_content = ""
            for line in read_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace(
                    self.ACTIVATED_KEY, self.DEACTIVATE_KEY)
                new_file_content += new_line + "\n"
            read_file.close()

            with open(self.FILEPATH, self.OPEN_MODE) as write_file:
                write_file.write(new_file_content)

            self.status = True

        elif self.contents[0] == f"{self.DEACTIVATE_KEY}\n":
            print("File already deactivated")
            self.status = True

        else:
            unknown_key = self.contents[0]
            print(f"Error: {unknown_key}Is an unknown key")

            self.status = False
