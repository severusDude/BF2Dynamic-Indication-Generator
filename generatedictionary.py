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

    # def dict_act(self, name, indi, wep_index):
    #     try:
    #         with open('game\\weapons.py', 'r+') as f:
    #             print(f.readlines())
    #             self.dict_add(wep_index, f)
    #     except FileNotFoundError as e:
    #         print(f"Dictionary file doesn't exist {e}")
    #         return False
    #     finally:
    #         f.close()

    # def dict_add(self, key, file):
    #     contents = file.readlines()
    #     text_line, index_line = self.find_dict_loc(key, contents)
    #     print(f"text line type is {type(text_line)} and index {text_line}")
    #     print(f"text line type is {type(index_line)} and index {index_line}")

    # def find_dict_loc(self, dict_item, file):
    #     dict_item -= 1
    #     print("step 1")
    #     for num_line, line in enumerate(file):
    #         print("step 2")
    #         if dict_item in line:
    #             print(
    #                 f"dict_item contain {dict_item} is on line number {num_line}")
    #             print(line)
    #             return line, num_line

    #     return -1

    def dict_add(self, file, index, name, indi):
        contents = file.readlines()
        text_line, req_index, line_num = self.find_dict_loc(contents, index)
        print(line_num)

        req_index = int(req_index)
        contents.insert(line_num,
                        f"		\"{name}\"			 : {index},		 # {indi}\n")
        contents = "".join(contents)
        file.write(contents)
        return contents

    def find_dict_loc(self, file, index):
        index_str = index - 1
        index_str = str(index_str)
        for num, line in enumerate(file, 1):
            if index_str in line:
                print(f"it here {index_str}")
                return line, index_str, num


x = GenerateDictionary()
x.init("bf4_scar_sv", 16, "SCAR SV")
