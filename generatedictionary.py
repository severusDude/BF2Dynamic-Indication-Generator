class GenerateDictionary:
    def init(self, name, index, indi):
        self.NAME = name
        self.INDEX = index
        self.INDI = indi
        self.STRING = f"		\"{name}\"			 : {index},		 # {indi}\n"
        self.DICT_PATH = 'game\\weapons.py'
        self.open_dict()

    # open dictionary file
    def open_dict(self):
        try:
            with open(self.DICT_PATH, 'r+') as f:
                self.dict_add(f, self.INDEX, self.NAME, self.INDI)
        except FileNotFoundError as e:
            print(f"Dictionary file doesn't exist {e}")
        finally:
            f.close()

    # add dictionary from user input
    def dict_add(self, file, index, name, indi):
        contents = file.readlines()
        text_line, req_index, line_num = self.find_dict_loc(contents, index)
        print(line_num)

        req_index = int(req_index)
        contents.insert(line_num, self.STRING)
        contents = "".join(contents)
        del_file = self.clear_dict(file)
        file.write(contents)
        return contents

    # find line number for placing dictionary
    def find_dict_loc(self, file, index):
        index_str = index - 1
        index_str = str(index_str)
        for num, line in enumerate(file, 1):
            if index_str in line:
                print(f"it here {index_str}")
                return line, index_str, num

    # clear file to prevent duplicate generate
    def clear_dict(self, del_contents):
        del_contents.read().split("\n")
        del_contents.seek(0)
        del_contents.truncate()
        return del_contents
