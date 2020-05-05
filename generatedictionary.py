import re


class GenerateDictionary:
    def init(self, name, index, indi):
        self.NAME = name
        self.INDEX = index
        self.INDI = indi
        self.STRING = f"		\"{name}\"			 : {index},		 # {indi}\n"
        self.DICT_PATH = 'game\\weapons.py'
        self.PATTERN = r' .*?,'
        self.FORBID_CHAR = [' ', ':', ',']
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

        indi_num = list()

        for item in contents:
            item = item.replace('\n', '')

            find_item = re.finditer(self.PATTERN, item)

            for item in find_item:
                item = item.group(0)

                for char in self.FORBID_CHAR:
                    if char in item:
                        item = item.replace(char, '')

                indi_num.append(item)

                print(item)

        max_num = self.get_max(indi_num)

        for num, line in enumerate(contents, 1):
            if str(index - 1) in line:
                num_line = num
                not_exist = False
                break

            elif str(max_num) in line:
                max_num_line = num
                not_exist = True

        if not_exist:
            print(
                f"Highest indicator is {max_num} located in line {max_num_line}")
            contents.insert(max_num_line, self.STRING)

        else:
            print(f"Indicator {index - 1} located in {num_line}")
            contents.insert(num_line, self.STRING)

        contents = "".join(contents)

        self.clear_dict(file)

        file.write(contents)
        return contents

    def get_max(self, lst):
        mx = int()

        for num in lst:
            if int(num) > mx:
                mx = int(num)

        return mx

    # clear file to prevent duplicate generate
    def clear_dict(self, del_contents):
        del_contents.read().split("\n")
        del_contents.seek(0)
        del_contents.truncate()
        return del_contents


# x = GenerateDictionary()
# x.init("eu_famas", 234, "FAMAS")
