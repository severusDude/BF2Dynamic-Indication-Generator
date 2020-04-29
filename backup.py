import datetime
import fnmatch
import shutil
import os


class BackupFiles:
    def init(self, dir_path, indi_dir_path, dict_dir_path):

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        backup_file = fnmatch.filter(os.listdir(dir_path), '*.zip')
        backup_file_count = len(backup_file)

        if backup_file_count <= 5:
            self.listing_files(dir_path, indi_dir_path, dict_dir_path)
        elif backup_file_count == 6:
            os.remove(f"{dir_path}\\{backup_file[0]}")
            os.remove(f"{dir_path}\\{backup_file[1]}")
        else:
            os.remove(f"{dir_path}\\{backup_file[0]}")

    def listing_files(self, dir_path, indi_dir_path, dict_dir_path):
        req_file_1 = fnmatch.filter(os.listdir(indi_dir_path), '*.con')
        req_file_2 = fnmatch.filter(os.listdir(dict_dir_path), '*.py')

        current_time = datetime.datetime.now().strftime("%d-%m-%Y %H.%M")
        temp = 'temp'
        generated_folder = f'Backup_{current_time}'
        generated_folder_loc = f"{temp}\\{generated_folder}"
        dir_path = f"{dir_path}\\{generated_folder}"

        if not os.path.exists(temp):
            os.makedirs(temp)
        if not os.path.exists(generated_folder_loc):
            os.makedirs(generated_folder_loc)

        req_temp_list = list()
        self.status = bool()

        try:
            for loop_file in req_file_1:
                loop_file = f"{indi_dir_path}\\{loop_file}"
                if os.path.exists(loop_file):
                    shutil.copy(loop_file, generated_folder_loc)
                    req_temp_list.append(loop_file)
                else:
                    print(f"error at {loop_file}")

            if len(req_temp_list) == len(req_file_1):
                self.status = True
            else:
                self.status = False

        except:
            print("Failed to generate")

        if self.status:
            req_file_2[0] = f"{dict_dir_path}\\{req_file_2[0]}"
            shutil.copy(req_file_2[0], generated_folder_loc)

        indi_files = fnmatch.filter(os.listdir(generated_folder_loc), '*.con')
        dict_file = fnmatch.filter(os.listdir(generated_folder_loc), '*.py')
        count_files = len(indi_files + dict_file)

        # print(f"type {type(generated_folder)} content {generated_folder}")
        # print(
        #     f"type {type(generated_folder_loc)} content {generated_folder_loc}")
        # print(f"type {type(indi_files)} content {indi_files}")
        # print(f"type {type(dict_file)} content {dict_file}")
        # print(f"type {type(count_files)} content {count_files}")
        # print(f"type {type(req_file_1)} content {req_file_1}")
        # print(f"type {type(req_file_2)} content {req_file_2}")
        # print(f"type {type(req_temp_list)} content {req_temp_list}")
        print(dir_path)
        print(f"{generated_folder_loc}")

        if count_files == 8:
            succes = self.compress_files(dir_path, generated_folder_loc, temp)
            # if succes:
            #     print("succes")
            # else:
            #     print("failed")
        else:
            print(f"Required file missing")

    def compress_files(self, output_dir, dir_name, del_dir):
        shutil.make_archive(output_dir, 'zip', dir_name)
        # if not os.path.exists(output_dir):
        #     return False
        # else:
        # if not os.path.exists(f"{dir_name}"):
        #     return False
        # else:
        shutil.rmtree(del_dir)
        #     return True
        # return True


x = BackupFiles()
print(x.init('backups', 'HUD\\HudSetup\\Killtext', 'game'))
