import datetime
import fnmatch
import shutil
import os


class BackupFiles:
    def __init__(self, req_dir1_path, req_dir2_path, backup_fileslimit):
        self.BACKUP_DIR_PATH = 'backups'
        self.TEMP_DIR_PATH = 'temp'
        self.BACKUP_FILESLIMIT = backup_fileslimit
        self.DIR1_FILETYPE = '*.con'
        self.DIR2_FILETYPE = '*.py'
        self.REQ_DIR1_PATH = req_dir1_path
        self.REQ_DIR2_PATH = req_dir2_path
        self.dir1_filelist = list()
        self.dir2_filelist = list()
        self.backup_files = list()
        self.backup_files_count = int()
        self.temp_dirs = list()
        self.temp_dirs_count = int()
        self.status = bool()
        self.compress_succes = bool()

        self.current_time = datetime.datetime.now().strftime("%d-%m-%Y %H.%M")
        # output will be (day)-(month)-(year) (hour).(minute)

        self.backup_filename = f'Backup_{self.current_time}'
        # output will be Backup_(day)-(month)-(year) (hour).(minute)

        self.gen_backupfile_path = f'{self.BACKUP_DIR_PATH}\\{self.backup_filename}'
        # output will be backups\Backup_(current_time)

        self.gen_backupdir_path = f'{self.TEMP_DIR_PATH}\\{self.backup_filename}'
        # output will be temp\Backup_(current_time)

        # call self.init() to start system
        if len(self.REQ_DIR1_PATH) and len(self.REQ_DIR2_PATH) > 0:
            self.init()

    # start the whole system
    def init(self):
        if not os.path.exists(self.BACKUP_DIR_PATH):
            os.makedirs(self.BACKUP_DIR_PATH)

        self.backup_files = fnmatch.filter(
            os.listdir(self.BACKUP_DIR_PATH), '*.zip')
        self.backup_files_count = len(self.backup_files)

        if self.backup_files_count > self.BACKUP_FILESLIMIT:
            os.remove(f"{self.BACKUP_DIR_PATH}\\{self.backup_files[0]}")

        self.listing_files()

    # list files that are inside given directiories
    def listing_files(self):
        self.dir1_filelist = fnmatch.filter(os.listdir(
            self.REQ_DIR1_PATH), self.DIR1_FILETYPE)
        self.dir2_filelist = fnmatch.filter(os.listdir(
            self.REQ_DIR2_PATH), self.DIR2_FILETYPE)

        self.copy_file()

        filelist_type1 = fnmatch.filter(os.listdir(
            self.gen_backupdir_path), self.DIR1_FILETYPE)
        filelist_type2 = fnmatch.filter(os.listdir(
            self.gen_backupdir_path), self.DIR2_FILETYPE)
        count_files = len(filelist_type1) + len(filelist_type2)

        if count_files == 8:
            self.compress_succes = self.compress_files(
                self.gen_backupfile_path, self.gen_backupdir_path)
        else:
            print("Required file missing")

    # copy listed files into a temporary backup folder
    def copy_file(self):

        if not os.path.exists(self.TEMP_DIR_PATH):
            os.makedirs(self.TEMP_DIR_PATH)
        if not os.path.exists(self.gen_backupdir_path):
            os.makedirs(self.gen_backupdir_path)

        self.temp_dirs = os.listdir(self.TEMP_DIR_PATH)
        self.temp_dirs_count = len(self.temp_dirs)

        tempdir1_list = list()
        tempdir2_list = list()

        try:
            for dir1_loop in self.dir1_filelist:
                dir1_loop = f'{self.REQ_DIR1_PATH}\\{dir1_loop}'
                if os.path.exists(dir1_loop):
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
                dir2_loop = f'{self.REQ_DIR2_PATH}\\{dir2_loop}'
                if os.path.exists(dir2_loop):
                    shutil.copy(dir2_loop, self.gen_backupdir_path)
                else:
                    print(f"error at {dir2_loop}")

            if len(tempdir2_list) == len(self.dir2_filelist):
                self.status = True
            else:
                self.status = False
        else:
            print("Required condition is not meet")

    # compress temporary backup folder and erased the temporay backup folder
    def compress_files(self, backup_filename, backup_dirsource):
        shutil.make_archive(backup_filename, 'zip',
                            backup_dirsource)

        gen_succes = bool()

        if os.path.exists(f'{backup_filename}.zip'):
            gen_succes = True
        else:
            gen_succes = False

        if gen_succes:
            shutil.rmtree(self.TEMP_DIR_PATH)
            return True
        else:
            return False
