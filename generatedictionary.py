class GenerateDictionary:
    def init(self, name, index, indi):
        self.name = name
        self.index = index
        self.indi = indi
        self.open_dict()

    def open_dict(self):
        try:
            with open('game\\weapons.py', 'r+') as f:
                self.dict_add(f, self.index, self.name, self.indi)
        except FileNotFoundError as e:
            print(f"Dictionary file doesn't exist {e}")
        finally:
            f.close()

    def dict_add(self, file, index, name, indi):
        contents = file.readlines()
        text_line, req_index, line_num = self.find_dict_loc(contents, index)
        print(line_num)

        req_index = int(req_index)
        contents.insert(line_num,
                        f"		\"{name}\"			 : {index},		 # {indi}\n")
        contents = "".join(contents)
        del_file = self.clear_dict(file)
        file.write(contents)
        return contents

    # def find_dict_loc(self, file, index):
    #     print("yes")
    #     index_str = index - 1
    #     for num, line in enumerate(file, 1):
    #         if str(index_str) in line:
    #             print(f"it here {index_str}")
    #             return line, index_str, num

    def find_dict_loc(self, file, index):
        index_str = index - 1
        index_str = str(index_str)
        for num, line in enumerate(file, 1):
            if index_str in line:
                print(f"it here {index_str}")
                return line, index_str, num

    def clear_dict(self, del_contents):
        del_contents.read().split("\n")
        del_contents.seek(0)
        del_contents.truncate()
        return del_contents


# x = GenerateDictionary()
# x.init("bf4_scar_sv", 129, "SCAR SV")
