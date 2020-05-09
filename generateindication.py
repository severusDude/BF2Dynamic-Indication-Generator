class GenerateIndication:
    # init generate indication
    def init(self, wep_index):
        self.WEP_INDEX = wep_index
        self.INDEX_START = 1
        self.INDEX_END = 7
        self.OPEN_MODE = 'r+'
        self.INDI_PATH = 'HUD\\HudSetup\\KillText'

        for page in range(self.INDEX_START, self.INDEX_END):
            self.indi1_act(self.WEP_INDEX, page)
        self.indi2_act(self.WEP_INDEX)

    # open indication files 1-6
    def indi1_act(self, index, file_index):
        try:
            with open(f'{self.INDI_PATH}\\CustomizeIndication{file_index}Weapon.con', self.OPEN_MODE) as f:
                f.readlines()
                self.write_indi(f, "kill", file_index, index)

        except FileNotFoundError as e:
            print(
                f"Required {self.INDI_PATH}\\CustomizeIndication{file_index}Weapon.con file not exist {e}")
            return False
        finally:
            f.close()

    # open attacker weapon file
    def indi2_act(self, index):
        try:
            with open(f'{self.INDI_PATH}\\HudElementsAttackerWeapon.con', self.OPEN_MODE) as f:
                f.readlines()
                self.write_indi(f, "dead", 0, index)
        except FileNotFoundError as e:
            print(
                f"Required file {self.INDI_PATH}\\HudElementsAttackerWeapon.con file doesn't exist {e}")
        finally:
            f.close()

    # write indication and attacker weapon
    def write_indi(self, file, key, indi_page, indi_index):
        kill_string = f"\nhudBuilder.createPictureNode\tIngameHud Indication{indi_page}weapon{indi_index} 301 352 162 24\nhudBuilder.setPictureNodeTexture \tIngame/Killtext/Indication/Indicationweapon{indi_index}.dds\nhudBuilder.setNodeShowVariable\tDemoRecInterfaceShow\nhudBuilder.setNodeColor\t\t1 1 1 0.8\nhudBuilder.setNodeInTime\t0.15\nhudBuilder.setNodeOutTime\t0.2\nhudBuilder.addNodeMoveShowEffect\t0 90\nhudBuilder.addNodeAlphaShowEffect\nhudBuilder.addNodeBlendEffect\t\t7 2\n\n"
        dead_string = f"\nhudBuilder.createPictureNode\tIngameHud AttackerWeapon{indi_index} 378 496 216 32\nhudBuilder.setPictureNodeTexture \tIngame/Killtext/KilledIndication/KilledIndicationWeapon{indi_index}.dds\nhudBuilder.setNodeShowVariable\tDemoRecInterfaceShow\nhudBuilder.setNodeColor\t\t1 1 1 0.8\nhudBuilder.setNodeInTime\t0.2\nhudBuilder.setNodeOutTime\t0.1\n\nhudBuilder.addNodeAlphaShowEffect\nhudBuilder.addNodeBlendEffect\t\t7 2\n"

        if key == "kill":
            file.write(kill_string)
        elif key == "dead":
            file.write(dead_string)
        else:
            print("invalid key")
        return True
