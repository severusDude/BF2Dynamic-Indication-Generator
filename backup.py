import datetime
import fnmatch
import shutil
import os


class BackupFiles:
    def __init__(self, req_dir1_path, req_dir2_path):
        self.backup_dir_path = 'backups'
        self.temp_dir_path = 'temp'
        self.dir1_filetype = '*.con'
        self.dir2_filetype = '*.py'
        self.backup_filetype = '*.zip'
        self.req_dir1_path = req_dir1_path
        self.req_dir2_path = req_dir2_path
        self.dir1_filelist = list()
        self.dir2_filelist = list()
        self.backup_files = list()
        self.backup_files_count = int()
        self.temp_dirs = list()
        self.temp_dirs_count = int()
        self.status = bool()

        self.current_time = datetime.datetime.now().strftime("%d-%m-%Y %H.%M")
        # output will be (day)-(month)-(year) (hour).(minute)

        self.backup_filename = f'Backup_{self.current_time}'
        # output will be Backup_(day)-(month)-(year) (hour).(minute)

        self.gen_backupfile_path = f'{self.backup_dir_path}\\{self.backup_filename}'
        # output will be backups\Backup_(current_time)

        self.gen_backupdir_path = f'{self.temp_dir_path}\\{self.backup_filename}'
        # output will be temp\Backup_(current_time)

        if len(self.req_dir1_path) and len(self.req_dir2_path) > 0:
            self.init()

    def init(self):
        if not os.path.exists(self.backup_dir_path):
            os.makedirs(self.backup_dir_path)

        self.backup_files = fnmatch.filter(
            os.listdir(self.backup_dir_path), '*.zip')
        self.backup_files_count = len(self.backup_files)

        print(self.backup_files)
        print(self.backup_files_count)

        if self.backup_files_count > 5:
            os.remove(f"{self.backup_dir_path}\\{self.backup_files[0]}")

        self.listing_files()

    def listing_files(self):
        self.dir1_filelist = fnmatch.filter(os.listdir(
            self.req_dir1_path), self.dir1_filetype)
        self.dir2_filelist = fnmatch.filter(os.listdir(
            self.req_dir2_path), self.dir2_filetype)

        self.copy_file()

        filelist_type1 = fnmatch.filter(os.listdir(
            self.gen_backupdir_path), self.dir1_filetype)
        filelist_type2 = fnmatch.filter(os.listdir(
            self.gen_backupdir_path), self.dir2_filetype)
        count_files = len(filelist_type1) + len(filelist_type2)

        if count_files == 8:
            compress_succes = self.compress_files(
                self.gen_backupfile_path, self.gen_backupdir_path)
        else:
            print("Required file missing")

    def copy_file(self):

        if not os.path.exists(self.temp_dir_path):
            os.makedirs(self.temp_dir_path)
        if not os.path.exists(self.gen_backupdir_path):
            os.makedirs(self.gen_backupdir_path)

        self.temp_dirs = os.listdir(self.temp_dir_path)
        self.temp_dirs_count = len(self.temp_dirs)

        tempdir1_list = list()
        tempdir2_list = list()

        try:
            for dir1_loop in self.dir1_filelist:
                dir1_loop = f'{self.req_dir1_path}\\{dir1_loop}'
                if os.path.exists(dir1_loop):
                    print(dir1_loop)
                    shutil.copy(dir1_loop, self.gen_backupdir_path)
                    tempdir1_list.append(dir1_loop)
                else:
                    print(f"error at {dir1_loop}")

            if len(tempdir1_list) == len(self.dir1_filelist):
                self.status = True
            else:
                self.status = False

        except:
            print("Failed to generate")

        if self.status:
            self.status = False
            for dir2_loop in self.dir2_filelist:
                dir2_loop = f'{self.req_dir2_path}\\{dir2_loop}'
                if os.path.exists(dir2_loop):
                    print(dir2_loop)
                    shutil.copy(dir2_loop, self.gen_backupdir_path)
                else:
                    print(f"error at {dir2_loop}")

            if len(tempdir2_list) == len(self.dir2_filelist):
                self.status = True
            else:
                self.status = False
        else:
            print("goddam")

    def compress_files(self, backup_filename, backup_dirsource):
        shutil.make_archive(backup_filename, 'zip',
                            backup_dirsource)

        for file in self.backup_files:
            if file == f'{self.backup_filename}.zip':
                print(f"Backup {file} is succesfully generated")
                gen_succes = True

        if gen_succes:
            shutil.rmtree(self.temp_dir_path)
            return True
        else:
            return False
